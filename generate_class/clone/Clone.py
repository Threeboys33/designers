# --*-- encode : utf-8 --*--
from copy import copy, deepcopy


class Animal:
    pass


class Dog(Animal):

    def __init__(self,name):
        self._name = name

    def create_dog(self,num):
        self._name = f"dog_{str(num)}"

    def change_name(self,name):
        self._name = f"dog__{str(name)}"

    def __str__(self):
        return f"{self._name} is dog animal "


class CopyTarget:  # 考虑深拷贝，浅拷贝

    def __init__(self):
        print("target create")
        self.copy_list = [Dog(f"dog{i}") for i in range(0, 3)]

    def change(self,index):
        self.copy_list[index].change_name(index + 10)

    def __str__(self):
        string_str = ""
        for i in range(len(self.copy_list)):
            string_str += str(self.copy_list[i])
        return string_str


if __name__ == '__main__':
    target = CopyTarget()
    #  浅拷贝的时候会对对象的引用对象进行引用复制
    copy_target = copy(target)
    #  深拷贝的时候会对对象的引用类容进行完全复制
    deep_target = deepcopy(target)
    for i in range(0, 3):
        target.change(i)
    print(copy_target)
    print(deep_target)
