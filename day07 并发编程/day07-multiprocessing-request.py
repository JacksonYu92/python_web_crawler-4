import time
#模拟网络请求的函数
# def get_request(url): #阻塞/耗时操作
#     print('正在请求网址的数据：', url)
#     time.sleep(2)
#     print('请求结束：', url)
#
# if __name__ == "__main__":
#     start = time.time()
#     urls = ['www.1.com', 'www.2.com', 'www.3.com']
#     for url in urls:
#         get_request(url)
#     end = time.time()
#     print('总耗时：', end - start)

from multiprocessing import Process
def get_request(url): #阻塞/耗时操作
    print('正在请求网址的数据：', url)
    time.sleep(2)
    print('请求结束：', url)

if __name__ == "__main__":
    start = time.time()
    urls = ['www.1.com', 'www.2.com', 'www.3.com']
    p_list = [] #存储创建好的所有的子进程
    for url in urls:
        p = Process(target=get_request, args=(url,))
        p_list.append(p)
        p.start()

    #让主进程等待所有子进程结束之后再结束
    for p in p_list:
        p.join() #每一个子进程都被join之后，才可以实现主进程等待子进程结束后再结束
    end = time.time()
    print('总耗时：', end - start)
