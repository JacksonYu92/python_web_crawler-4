import requests

img_url = 'https://t7.baidu.com/it/u=4162611394,4275913936&fm=193&f=GIF'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',

}
response = requests.get(url=img_url, headers=headers)

# 获取图片的响应数据
img_data = response.content #content是范围二进制形式的响应数据

with open('dog.jpg', 'wb') as fp:
    fp.write(img_data)