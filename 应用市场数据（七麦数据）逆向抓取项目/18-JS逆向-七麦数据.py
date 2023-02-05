import execjs
import requests
from urllib.parse import quote

'''
总榜: genre: '36'
应用: genre: '5000'
游戏: genre: '6014'
'''
genre = '36'
with open('./18-JS逆向-七麦数据.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
funcs = execjs.compile(js_code)
analysis = funcs.call('get_analysis', genre)
# print(analysis)

def parse_json_data(data):
   df = data['data']
   return {
      df[0]['brand_name']: df[0]['app_list'],
      df[1]['brand_name']: df[1]['app_list'],
      df[2]['brand_name']: df[2]['app_list']
   }
   df1 = data['data'][0]

url_format = 'https://api.qimai.cn/indexV2/getIndexRank?analysis={}&setting=0&genre={}'

headers = {
    'origin': 'https://www.qimai.cn',
    'referer': 'https://www.qimai.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
# 构造URL
url = url_format.format(quote(analysis), genre)
response = requests.get(url=url, headers=headers)
if response.status_code == 200:
   response.encoding = 'utf-8'
   data = parse_json_data(response.json())
   for d in data.keys():
      print(d)
      for i in data[d]:
         print(i)
else:
   print('请求失败, 状态码为{}'.format(str(response.status_code)))