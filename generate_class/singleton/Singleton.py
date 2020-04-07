import threading
import time


class Father(object):  # 单实例构建和初始化
    def __new__(cls, *args, **kwargs):
        # 此处添加的是类的变量
        if not hasattr(cls, "_instance"):
            # 通过调用super的__new__方法构建指定类的实例
            # cls._instance = super(Singleton, cls).__new__(cls,*args,**kwargs)
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance
    # 父类 类成员变量
    # 在定义时，按照父类和子类的顺序依次执行
    print("father variables")


class Son(Father):
    # 获取锁
    lock = threading.RLock()

    def exec_cmd(self, data):
        self.lock.acquire()
        time.sleep(1)
        print("Send signal data...", data)
        self.lock.release()

    # 初始化通过继承父类的__new__方法创建的该子类对象
    def __init__(self):
        self.lock.acquire()
        print("son init")
        self.lock.release()

    # 子类 类的成员变量
    print("son variables")


class CallSon(threading.Thread):
    target_son = ""
    cmd = ""

    def get_cmd(self):
        return self.cmd

    def set_cmd(self, cmd):
        self.cmd = cmd

    def run(self):
        self.target_son = Son()
        self.target_son.exec_cmd(self.get_cmd)
        # 确认该对象实例是否拥有的是同一Son对象实例
        print(f"bus id {id(self.target_son)}")


if __name__ == "__main__":
    for i in range(3):
        print("Entity %d begin to run..." % i)
        callson = CallSon()
        callson.set_cmd("Son_" + str(i))
        # 开启线程
        callson.start()
        # 等待线程完毕
        callson.join()
        print(f"{id(callson.target_son)},{type(callson.target_son)}")
