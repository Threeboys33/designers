#  装饰器的功能是对原有类的状态和行为进行扩展，返回的还是对象本身
#  代理模式是对类的行为进行控制，类真实的行为是隐藏起来的，对外不可见
#  本目录下python装饰器学习，通过单例和属性property做已记录


class PropertyWrapper(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, objtype=None):
        print("in __get__")
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(instance)

    def __set__(self, instance, value):
        print("in __set__")
        if self.fset is None:
            raise AttributeError
        self.fset(instance, value)

    # def __del__(self, instance):
    #     # print("in __del__")
    #     # if self.fdel is None:
    #     #     raise AttributeError
    #     # self.fdel(instance)
    #     pass

    def getter(self, fget):
        print("in getter")
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        print("in setter")
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        print("in deleter")
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class Student:
    def __init__(self, name):
        self.name = name

    #  此描述符在类定义的时候会进行，PropertyWrapper的实例初始化，并将math属性绑定
    @PropertyWrapper
    def math(self):
        return self._math

    #  此setter方法会在类定义的时候，调用setter方法，并产生一个新的propertywrapper实例，并赋值给类或者实例的__dict__
    @math.setter
    def math(self, value):
        if 0 <= value <= 100:
            self._math = value
        else:
            raise ValueError("valid value ")


if __name__ == '__main__':
    s = Student('三三')
    #  实例绑定type(s).__dict__['math'].__get__(s,type(s))
    #  type(s).__dict__['math'].__set__(s,88)
    #  对方法本来应该调用s.math()装饰成s.math
    s.math = 88
    print(s.math)