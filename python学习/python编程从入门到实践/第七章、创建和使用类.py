#### 7.1 创建和使用类
## 7.1.1 创建Dog类
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll(self):
        """模拟小狗被命令打滚"""
        print(self.name.title() + " rolled over.")

## 7.1.2 根据类创建实例
# my_dog = Dog('Willie', 6)
#
# print("My dog's name is "+ my_dog.name.title() + '.')  # 访问属性my_dog.name.title()
# print("My dog is "+ str(my_dog.age) + " years old.")
#
# my_dog.sit()  # 调用方法
# my_dog.roll()  # 调用小狗打滚方法

## 创建多个实例
# my_dog = Dog('Willie', 6)
# your_dog = Dog('lucy', 3)
#
# print("My dog's name is " + my_dog.name.title() + '.')  # 访问属性my_dog.name.title()
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
#
# print("\nYour dog's name is " + your_dog.name.title() + '.')  # 访问属性my_dog.name.title()
# print("Your dog is " + str(your_dog.age) + " years old.")
# your_dog.sit()

#### 7.2 使用类和实例
## 7.2.1 给属性指定默认值
# class Car():
#     """一次模拟汽车的简单尝试"""
#     def __init__(self, make, model, year):
#         """初始化描述汽车属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # 给属性指定默认值
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + " " + self.make.title() + " " + self.model.title()
#         return  long_name.title()
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading)+ " miles on it.")
#
#     def update_odometer(self, mileage):
#         """将里程表读数设置为指定的值"""
#         self.odometer_reading = mileage
#
# my_car = Car('audi', 'a4', 2016)
# print(my_car.get_descriptive_name())
# my_car.read_odometer()  # 调用方法
#
# ## 7.2.2 直接修改属性的值
# my_car.odometer_reading = 23
# my_car.read_odometer()
#
# ## 7.2.3 通过方法修改属性的值
# ## 见update_odometer方法
# my_car.update_odometer(25)
# my_car.read_odometer()

#### 7.3 继承
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make.title() + " " + self.model.title()
        return  long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading)+ " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
         print('You can not roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)  # super是一个特殊的函数，将父类与子类联系在一起。
        self.battery = Battery()  # 将实例用作属性


my_tesla = ElectricCar('tesela', 'model s', 2016)
print(my_tesla.get_descriptive_name())

## 给子类定义属性和方法
## 添加新属性self.battery_size.
# my_tesla.describe_battery()

## 将实例用作属性
my_tesla.battery.describe_battery()
















