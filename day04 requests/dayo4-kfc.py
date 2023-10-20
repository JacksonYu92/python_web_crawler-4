import requests

url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Referer': 'https://www.kfc.com.cn/kfccda/storelist/index.aspx'
}
keyword = input("Please input city name: ")
data = {
    'cname': '',
    'pid': '',
    'keyword': keyword,
    'pageIndex': '1',
    'pageSize': '10',
}
response = requests.post(url=url, headers=headers, data=data)

page_text = response.json()

for dict in page_text['Table1']:
    storeName = dict['storeName']
    addressDetail = dict['addressDetail']
    print(f"{storeName}:{addressDetail}")
