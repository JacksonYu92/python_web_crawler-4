from multiprocessing.dummy import Pool #线程池
import time
urls = ['www.1.com','www.2.com','www.3.com','www.4.com','www.5.com']
def get_reqeust(url):
    print('正在请求数据：',url)
    time.sleep(2)
    print('请求结束:',url)
start = time.time()

if __name__ == '__main__':
    # 创建线程池
    pool = Pool(5) #线程池中会产生5个可重复利用的线程

    # 将urls列表中的每一个列表元素依次作为参数传递给get_request函数
    #get_request调用的次数取决于urls列表元素的个数
    #map会将每一个get_request绑定给线程池中的某一个线程对象
    pool.map(get_reqeust, urls)
    print('总耗时：',time.time()-start)
