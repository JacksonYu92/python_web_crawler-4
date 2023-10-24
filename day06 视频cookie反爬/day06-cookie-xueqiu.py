import requests
#session对象会实时保存跟踪服务器端创建的cookie



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    # 'Cookie':'cookiesu=161693875396237; device_id=2e8cf6037c6a9d5d18d6ccd6a3155bbb; s=c71kx6j3n4; __utma=1.1148205069.1695649504.1695649504.1695649504.1; __utmz=1.1695649504.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); acw_tc=2760825e16981334019123441eb80eb085de28431dc50a9c7b09de15661893; xq_a_token=e2f0876e8fd368a0be2b6d38a49ed2dd5eec7557; xqat=e2f0876e8fd368a0be2b6d38a49ed2dd5eec7557; xq_r_token=2a5b753b2db675b4ac36c938d20120660651116d; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcwMDY5OTg3NSwiY3RtIjoxNjk4MTMzMzY1NDE1LCJjaWQiOiJkOWQwbjRBWnVwIn0.aZQZGyoluh9OVU5WhiDE9uHJW2eozFUndSuERSOrlyFNf25AknuWNGx7pUse9PA8NVFTFT-QPnNUX8fQYt_gZdu9NLOAm5-fapQfmpzFR6-ocT5AAISMLIbUI0J4PWJWegradDL2ny7XeKAfhX-absRbxTYC701VyVoKyqnzD6vCNMv_K2ymdNk9tUf0Wo17SNwWuKd5OnVGAwEHQcvIyKTrsxgjmXessfS5QeOy_APB-ZfChBZtopCjrCtnTsiQwsWLGm-8GvbLX1j3GRvbkXsO638mm39fo8rYirpbfNUOxNmUB8xF4zhLycFy_vBWNmGOXGj9QwTcYRlmdbd8Wg; u=161693875396237; Hm_lvt_1db88642e346389874251b5a1eded6e3=1695649478,1698133404; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1698133998'
}
param = {
    # 如果遇到了动态变化的请求参数？必须经过测试才知道需不需要处理
    'since_id': '-1',
    'max_id': '553800', #动态变化的请求参数
    'size': '25'
}
url = 'https://xueqiu.com/statuses/hot/listV2.json'

#创建一个session对象
session = requests.Session() #空白哦session对象
first_url = 'https://xueqiu.com/'
#使用session对象进行请求发送: 如果该次请求时，服务器端给客户端创建cookie的话，则该cookie就会被保存到当前session当中
session.get(url=first_url, headers=headers)
# session.cookies.get()
#使用保存了cookie的session对象进行后续请求发送

ret = session.get(url=url, headers=headers,params=param).json()
print(ret)

#原因1：动态变化的请求参数max_id
#原因2：模拟浏览器的力度（请求头）