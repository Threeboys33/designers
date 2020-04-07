import random

class test:
    def __new__(cls, *args,**kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(test, cls).__new__(cls,*args,**kwargs)
        return cls._instance

if __name__ == '__main__':
    # t = test()
    # print(type(t))
    # if not hasattr(t, "_instance"):
    #     print("no")
    # else:
    #     print("yes")
    hasattr('id')

    list = []
    for i in range(0,10):
        list.append(round(random.uniform(16,20),1))
    list.sort()

    for i in range(0,10):
        print(list[i])







