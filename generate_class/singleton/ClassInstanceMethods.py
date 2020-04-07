#类方法和实例方法的__new__、__init__

class Animal:
    def __new__(cls, name):
        print(f"This is Animal class ,cls is instance of {cls.__class__}")
        print("调用super类的__new__方法构造实例")
        super(Animal, cls).__new__(cls,name)
