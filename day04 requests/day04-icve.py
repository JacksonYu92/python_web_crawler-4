import requests

url = 'https://www.icve.com.cn/portal/course/getNewCourseInfo'
data = {
    'kczy': '',
    'order': '',
    'printstate': '',
    'keyvalue': '',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Referer':'https://www.icve.com.cn/portal_new/course/course.html',
}
response = requests.post(url=url, headers=headers, data=data)

#json()可以直接将请求到的响应数据进行反序列化
page_text = response.json()

#解析人名
for dic in page_text['list']:
    name = dic['TeacherDisplayname']
    print(name)