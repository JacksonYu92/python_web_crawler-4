import requests

#1.指定url
#url中?后面的内容就是【请求参数】
#处理请求参数
game_title = input('enter a game title: ')
param = {
    'q': game_title
}
first_url = 'https://game.51.com/search/action/game/'

#2.发请求（携带请求参数）
response = requests.get(url=first_url, params=param)

#3.获取响应数据
page_text = response.text

#4.持久化存储
file_name = game_title + '.html'
with open(file_name, 'w') as fp:
    fp.write(page_text)