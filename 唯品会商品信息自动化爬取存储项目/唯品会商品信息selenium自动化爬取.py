'''
网址: https://www.vip.com/
# 唯品会搜索商品信息获取
# 搜索口红，并获取数据
地址: https://category.vip.com/suggest.php?keyword=%E5%8F%A3%E7%BA%A2&ff=235|12|1|1
技术: selenium自动化
字段: 价格、标题   可以自行拓展
保存: mongo
交付: 数据入库截图
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import random

import pymongo

class WeiPinHui(object):
    def __init__(self, search_keyword):
        self.search_keyword = search_keyword
        self.url = 'https://www.vip.com'

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        self.options.add_argument('user-agent={}'.format(user_agent))
        self.options.add_argument('-ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.maximize_window()

    # 连接MongoDB数据库
    def link_mongo(self):
        client = pymongo.MongoClient(host='localhost', port=27017)
        database_names = client.list_database_names()
        if 'weipinhui_db' not in database_names:
            print('[mongodb] weipinhui_db 数据库不存在, 创建新数据库! ')
        else:
            print('[mongodb] weipinhui_db 数据库已存在! ')
        weipinhui_db = client['weipinhui_db']
        collection_names = weipinhui_db.list_collection_names()
        # 以搜索词作为数据集合的名称
        if self.search_keyword not in collection_names:
            print('[mongodb] [{}] 数据表不存在, 创建新数据表! '.format(self.search_keyword))
        else:
            print('[mongodb] [{}] 数据表已存在! '.format(self.search_keyword))
        table = weipinhui_db[self.search_keyword]
        return client, table

    # 保存数据
    def save_data(self, table, items):
        try:
            table.insert_many(items)
            print('mongodb 当前页数据爬取储存成功! ')
        except Exception as e:
            print('mongodb 数据插入失败: {}'.format(e))


    # 初始化页面资源
    def init_load(self, browser):
        browser.implicitly_wait(5)
        browser.get(self.url)
        browser.implicitly_wait(5)
        browser.find_element(by=By.XPATH, value='//input[@mars_sead="search_entrance_click"]').send_keys(self.search_keyword)
        time.sleep(3)
        browser.find_element(by=By.XPATH, value='//*[@id="J-search"]/div[1]/a').click()
        time.sleep(random.randint(1, 3))
        return browser

    # 加载资源
    def load_source(self, browser):
        for i in range(1, 11):
            time.sleep(random.randint(2, 3))
            browser.execute_script(f'window.scrollTo(0, document.body.scrollHeight * {i/10})')
        for i in range(15, 0, -1):
            time.sleep(random.randint(2, 3))
            browser.execute_script(f'window.scrollTo(0, document.body.scrollHeight * {i/15})')
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)
        return browser

    def parse_data(self, browser):
        browser.implicitly_wait(5)
        goods = browser.find_elements(by=By.XPATH, value='//*[@id="J_searchCatList"]/div/a')
        item_list = []
        for good in goods:
            item = {
                'title': good.find_element(by=By.XPATH, value='.//div[@class="c-goods-item-bottom    "]/div[2]').text,
                'price': good.find_element(by=By.XPATH, value='.//div[2]/div[1]/div/div[@class="c-goods-item__sale-price J-goods-item__sale-price"]').text,
                'cover_link': good.find_element(by=By.XPATH, value='.//div[@class="c-goods-item__img"]/img').get_attribute('src'),
                'good_link': good.get_attribute('href')
            }
            item_list.append(item)
        return browser, item_list

    # 判断下一页是否可以点击
    def just_next_page(self, browser):
        try:
            browser.find_element(by=By.ID, value='J_nextPage_link')
            current_page = browser.find_element(by=By.XPATH, value='.//span[@class="cat-paging-nub f-paging-default"]').text
            print('当前所处页数为: 第[{}]页, 开始爬取下一页'.format(current_page))
            try:
                iframe = browser.find_element(by=By.XPATH, value='//iframe[@class="login_iframe"]')
                browser.switch_to.frame(iframe)
                x_element = browser.find_element(by=By.CSS_SELECTOR, value='body > div > a.ui-dialog-close.vipFont.J-login-frame-close')
                x_element.click()
                browser.switch_to.default_content()
                print('弹出窗口, 点击关闭! ')
            except:
                pass
            return True
        except Exception as e:
            print('错误为: {}'.format(e))
            print('下一页不可点击')
            return False

    # 获取下一页
    def next_page(self, browser):
        if self.just_next_page(browser=browser):
            browser.find_element(by=By.ID, value='J_nextPage_link').click()
            return browser
        print('未找到下一页')
        return None

    def main(self):
        # 连接加载数据库
        client, table = self.link_mongo()
        # 加载保存首页信息
        browser = self.load_source(browser=self.init_load(browser=self.browser))
        browser, item_list = self.parse_data(browser=browser)
        self.save_data(table=table, items=item_list)
        # 加载保存后续页信息
        while True:
            browser_new = self.next_page(browser=browser)
            if browser_new is None:
                break
            browser_new = self.load_source(browser=browser_new)
            browser, item_list = self.parse_data(browser=browser_new)
            self.save_data(table=table, items=item_list)

        # 退出浏览器, 关闭数据库
        time.sleep(3)
        browser.quit()
        client.close()

if __name__ == '__main__':
    keyword = '手机'
    wei_pin_hui = WeiPinHui(search_keyword=keyword)
    wei_pin_hui.main()
