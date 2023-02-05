import execjs
import requests
import base64

target_url = 'https://dict.youdao.com/webtranslate'

headers = {
    "sec-ch-ua": '\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=126857516.95794569; OUTFOX_SEARCH_USER_ID=-1446782331@123.13.65.31; hb_MA-B0D8-94CBE089C042_source=www.baidu.com; YOUDAO_MOBILE_ACCESS_TYPE=0",
    'Host': 'dict.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
}
with open('./有道翻译逆向.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
js_funcs = execjs.compile(js_code)
data = eval(js_funcs.call('f'))
data['i'] = input('请输入要翻译的内容: ')
data['from'] = 'auto'
data['to'] = ''
data['domain'] = 0
data['dictResult'] = 'true'
data['keyid'] = 'webfanyi'
# print(data)
response = requests.post(url=target_url, headers=headers, data=data)
print(response.text)
print(len(response.text))
