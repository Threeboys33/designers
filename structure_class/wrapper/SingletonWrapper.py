#  装饰器的功能是对原有类的状态和行为进行扩展，返回的还是对象本身
#  代理模式是对类的行为进行控制，类真实的行为是隐藏起来的，对外不可见
#  本目录下python装饰器学习，通过单例和属性property做已记录

instances = {}


def singleton(cls):
    def get_instance(*args, ** kwargs):
        cls_name = cls.__name__
        print('_____1______')
        if not cls_name in instances:
            print('____2_____')
            instance = cls(*args, **kwargs)
            instances[cls_name] = instance
        return instances[cls_name]
    return get_instance


@singleton
class User:
    _instance = None

    def __init__(self, name):
        print('_____3______')
        self.name = name


if __name__ == '__main__':
    u1 = User('sansan1')
    #  第二个对象的创建并没有生效，从已有的set集合中取出
    u2 = User('sansan2')
    print(u1.name)
    print(u2.name)
    print(id(u1),id(u2))
    print(u1 == u2)
