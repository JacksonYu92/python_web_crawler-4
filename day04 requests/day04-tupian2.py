from urllib.request import urlretrieve

img_url = 'https://t7.baidu.com/it/u=4162611394,4275913936&fm=193&f=GIF'
# 参数1：图片地址
# 参数2： 图片存储路径
# urlretrieve可以根据图片地址将图片数据请求到直接存储到参数2表示的图片存储路径中
urlretrieve(img_url, "1.jpg")