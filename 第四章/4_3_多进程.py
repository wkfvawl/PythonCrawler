from multiprocessing import Process
import os

print("当前进程ID：", os.getpid())


# 定义一个函数，供主进程调用
def action(name, *add):
    print(name)
    for arc in add:
        print("%s --当前进程%d" % (arc, os.getpid()))


# 自定义一个进程类
class My_Process(Process):
    def __init__(self, name, *add):
        super().__init__()
        self.name = name
        self.add = add

    def run(self):
        print(self.name)
        for arc in self.add:
            print("%s --当前进程%d" % (arc, os.getpid()))


if __name__ == '__main__':
    # 定义为进程方法传入的参数
    my_tuple = ("test1",
                "test2",
                "test3")
    my_process = My_Process("my_process进程", *my_tuple)
    # 启动子进程
    my_process.start()
    # 主进程执行该函数
    action("主进程", *my_tuple)