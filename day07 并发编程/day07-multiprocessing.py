#主进程
from multiprocessing import Process

def func(a,b):
    print(a+b)
    print('我是新建进程绑定的任务')

if __name__ == '__main__':
    #新建了一个进程，给其绑定了一个具体的任务
    p = Process(target=func, args=(1,2))
    #启动子进程
    p.start()

    print('主进程执行结束')