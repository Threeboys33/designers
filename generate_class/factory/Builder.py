

class Screen:  # 屏幕
    def __init__(self, size):
        self._size = size


class LedScreen(Screen):  # LED屏幕
    def __init__(self,size,name):
        super(LedScreen, self).__init__(size)
        self._name = name

    def __str__(self):
        return f"name:{self._name!s} size:{self._size!s}"


class Power:  # 电源
    def __init__(self,weight):
        self._weight = weight


class FFPower(Power):  # 45功率电源
    def __init__(self,weight,power):
        super().__init__(weight)
        self._power = power

    def __str__(self):
        return f"power:{self._power!s} weight:{self._weight!s}"


class ComputerBuilder:  # 将computer的组成部件进行组装
    screen = None
    power = None

    @classmethod
    def build_screen(cls, Screen):
        cls.screen = Screen
        return cls

    @classmethod
    def build_power(cls, Power):
        cls.power = Power
        return cls

    @classmethod
    def build(cls):
        return Computer(cls)


class ComputerDirectory:
    computer_builder = None

    def __init__(self, ComputerBuilder):  # 根据传递进来的参数按照一定的顺序选取合适的构建
        self.computer_builder = ComputerBuilder

    def createComputer(self, Screen, Power):
        return self.computer_builder.build_screen(Screen).build_power(Power).build()


class Computer:
    screen = None
    power = None

    def __init__(self, computer_builder):
        Computer.screen = computer_builder.screen
        Computer.power = computer_builder.power

    def __str__(self):
        return f"computer is made of {self.screen!s}, {self.power!s}"


if __name__ == '__main__':
    # computer = ComputerBuilder.build_screen(LedScreen(27,'LED显示屏')).build_power(FFPower('2kg', '30kw')).build()
    computer = ComputerDirectory(ComputerBuilder()).createComputer(LedScreen(27,'LED显示屏'),FFPower('2kg', '30kw'))
    print(computer)

