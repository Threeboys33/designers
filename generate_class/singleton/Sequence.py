#实例化的顺序
#1、父类普通变量
#2、子类普通变量
#3、父类构造器
#4、子类构造器


class Father:  # 父类
    def __init__(self,name):
        self.name = name
        print(f"this is father constructor {self.__class__!s}  {name!s}")
    print(f"this is father normal number parameter")


class Son(Father):  # 子类
    def __init__(self,name):
        self.name = name
        super().__init__(name)
        # Father.__init__(self,name)
        print(f"this is son constructor {self.__class__!r} {name !s}")
    print("this is son normal number parameter")

if __name__ == '__main__':
    son = Son('san')