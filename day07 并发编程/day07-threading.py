from threading import Thread
import time


def get_request(url):
    print('正在请求：', url)
    time.sleep(2)
    print('请求结束：', url)

if __name__ == '__main__':
    start = time.time()
    urls = ['www.1.com', 'www.2.com', 'www.3.com']
    t_list = []
    for url in urls:
        # 创建线程
        t = Thread(target=get_request, args=(url,))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()
    print('总耗时：', time.time()-start)