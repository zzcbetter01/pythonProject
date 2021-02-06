#### 3.1 条件测试
cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':  # 检查是否相等
#         print(car.upper())
#     else:
#         print(car.title())

# for car in cars:
#     if car != 'bmw':  # 检查是否不相等
#         print(car.lower())
#     else:
#         print(car.title())

### 3.1.1 使用and或者or检查多个条件
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)  # 只有两个判断都是正确的，才会输出True
# print(age_0 >= 21 or age_1 >= 21)   # 两个判断只要有一个是正确的，就会输出True

### 3.1.2 检查特定值时候包含在列表中
# car1 = 'ji li'
# if car1 in cars:  # 这里用in或not in 进行判断元素是不是在列表中。
#     print(car1.title())
# else:
#     print(car1.lower())

### 3.1.3 if-elif-else结构
# 只执行一个代码块，如果要运行多个代码块，就使用一系列独立的if语句
# age = 12
# if age < 4:
#     print('Your admission cost is $0.')
# elif age < 18:
#     print('Your admission cost is $5.')
# else:
#     print('Your admission cost is $10.')

### 3.1.4 多个elif代码块
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 15
# else:
#     price = 10
# print('Your admission cost is '+'$'+str(price)+'!')

### 3.1.5 测试多个条件
# age = [12, 18, 25, 40]
# if 12 in age:
#     print("Adding 12")
# if 18 in age:
#     print("Adding 18")
# if 25 in age:
#     print("Adding 25")
# if 40 in age:
#     print("Adding 40")

#### 3.2 使用if语句处理列表
### 3.2.1 检查特殊元素
# for car in cars:
#     if car == 'bmw':
#         print('Sorry, we are out of bmw right now.')
#     else:
#         print('Now, we will buy this '+ car.title())
# print('\n Finished selecting it.')

### 3.2.2 确定列表不是空的
cars1 = []
# if cars1:  # 进行检查，判断列表是否为空
#     for car in cars1:
#         print('Now, we will buy this ' + car.title())
# else:
#     print('Are you sure you want a car?')

### 3.2.3 使用多个列表
available_cars = ['audi', 'bmw', 'subaru', 'toyota', 'ji li']
requested_cars = ['bmw', 'byd', 'ha fo']
for requested_car in requested_cars:
    if requested_car in available_cars:
        print("Your order " + requested_car.title() + " is available. ")
    else:
        print('Sorry, Your order ' + requested_car.title() + " is not available. ")