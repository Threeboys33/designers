from enum import Enum


class Commodity(Enum):  # 商品类别分类枚举
    shoe = 1
    clothing = 2
    appliance = 3


class Goods(object):  # 工厂模式 产品抽象类 abstract product
    def __init__(self, category, name, size):
        self._category = category
        self._name = name
        self._size = size

    @property  # 将实例的私有变量公开，可以通过instance.category进行调用，此处property是装饰器的注解，主要对category的get进行装饰
    def category(self):
        return self._category

    @category.setter
    def category(self,value):
        self._category = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._category = value

    @property
    def size(self):
        return self._size

    @size.setter
    def name(self, value):
        self.size = value

    def __str__(self) -> str:
        return f"Goods category :{self._category!s}, name : {self._name!s}, size : {self._size} \n" \
               "========================================================="


class Shoe(Goods):  # concrete product
    def __init__(self,  category=Commodity.shoe, name='鞋子',size=40):
        super().__init__(category,name, size)


class Clothing(Goods):  # concrete product
    def __init__(self, category=Commodity.clothing, name='上衣', size='l'):
        super().__init__(category, name, size)


class Appliance(Goods):  # concrete product
    def __init__(self, category=Commodity.appliance, name='家电', size='middle'):
        super().__init__(category, name, size)


class Factory:  # abstract factory
    goods = None

    @classmethod
    def create_product(cls,**kwargs):
        # 模板方式，具体实现有子类体现
        super(Factory, cls).__new__(cls, **kwargs).__init__()
        super(Factory,cls).__new__(cls,**kwargs).__call__(**kwargs)
        return cls

    def __call__(self, **kwargs):
        pass

    def __init__(self):
        pass


class ShoeFactory(Factory):  # concrete factory
    def __init__(self):
        print(f"I'am {self.__class__.__name__} going to making shoe")

    def __call__(self, **kwargs):
        Factory.goods = Shoe(**kwargs)


class ClothingFactory(Factory):  # concrete factory
    def __init__(self):
        print(f"I'am {self.__class__.__name__} going to making clothing")

    def __call__(self, **kwargs):
        Factory.goods = Clothing(**kwargs)


class ApplianceFactory(Factory):  # concrete factory
    def __init__(self):
        print(f"I'am {self.__class__.__name__} going to making appliance")

    def __call__(self, **kwargs):
        # 方法中有__call__ 变量的话相当于
        # instance = Object()
        # instance(**kwargs)方法调用
        Factory.goods = Clothing(**kwargs)


if __name__ == '__main__':
    # ShoeFactory()(category=Commodity.shoe, name='j17',size=40)
    print(ShoeFactory.create_product(category=Commodity.shoe, name='j17',size=40).goods)

    # ClothingFactory()(category=Commodity.clothing, name='夹克', size='xl')
    print(ClothingFactory.create_product(category=Commodity.clothing, name='夹克', size='xl').goods)

    # ApplianceFactory()(category=Commodity.appliance, name='compute', size='27')
    print(ApplianceFactory.create_product(category=Commodity.appliance, name='compute', size='27').goods)



