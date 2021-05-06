import threading

#创建子线程类，继承自 Thread 类
class my_Thread(threading.Thread):
    def __init__(self,add):
        threading.Thread.__init__(self)
        self.add = add
    # 重写run()方法
    def run(self):
         for arc in self.add:
            #调用 getName() 方法获取当前执行该程序的线程名
            print(threading.current_thread().getName() +" "+ arc)

#定义为 run() 方法传入的参数
my_tuple = ("test1",
            "test2",
            "test3")
#创建子线程
mythread = my_Thread(my_tuple)
#启动子线程
mythread.start()
#主线程执行此循环
for i in range(10):
    print(threading.current_thread().getName())

