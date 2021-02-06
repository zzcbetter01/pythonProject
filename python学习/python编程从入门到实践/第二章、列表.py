#### 2.1 列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

### 2.1.1 访问列表元素
# print(bicycles[0].title())  # 访问列表是从0开始，返回第一个元素
# print(bicycles[1])  # 返回第二个元素
# print(bicycles[-1])  # 返回列表最后一个元素

### 2.1.2 使用列表中的值
# message = "My first bicycle was a " + bicycles[0].title() +'.'
# print(message)

#### 2.2 修改、添加和删除元素
# bicycles[0] = 'fenghuang'  # 修改元素
# print(bicycles)

### 2.2.1 在末尾添加元素
# bicycles.append('trek')  # append表示在附加，在列表末尾
# print(bicycles)

### 2.2.2 在列表任意位置插入元素
# bicycles.insert(0, 'ducati')  # insert表示在列表任何位置添加新元素
# print(bicycles)

### 2.2.3 使用del语句删除元素
# del bicycles[0]  # 如果知道要删除的元素的位置，可使用del语句
# print(bicycles)  # 使用del删除元素时，就无法再次访问了

### 2.2.4 使用pop()删除元素
# new_bicycles = bicycles.pop()  # pop函数删除列表末尾的元素，
# print(new_bicycles)
# first_owned = bicycles.pop(2)  # pop函数其实可以删除任何位置的元素，只需要在pop中添加索引即可
# print('The first bicycle I owned was a '+ first_owned.title() +'.')

### 2.2.5 根据值删除元素
# bicycles.remove('trek')  # 如果知道要删除元素的值，可使用remove
# print(bicycles)  # 但是remove只删除第一个指定的值，如果列表中有多个重复元素，可以用循环，在第七章学习。

#### 2.4 组织列表

###  2.4.1 使用sort()对列表进行永久性排序
# bicycles.sort()  # 按首字母进行永久性排序
# print(bicycles)
#
# bicycles.sort(reverse=True)  # 按首字母顺序相反的顺序排列元素
# print(bicycles)

###  2.4.2 使用sorted()对列表进行临时排序
# print(sorted(bicycles))  # 临时排序，不影响原始元素顺序
# print(bicycles)

### 2.4.3 倒着打印列表
# print(bicycles)
# bicycles.reverse()  # 反转列表元素的排列顺序，并不是按字母顺序的相反顺序排列元素
# print(bicycles)
# print(len(bicycles))  # 获取列表长度


#### 2.5 遍历整个列表
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)
#     print(magician.title() + ", that was a great trick!"+'\n')
# print('Thank you, everyone. That was a great magic show.')

#### 2.6 创建数值列表
### 2.6.1 使用函数range()
# for value in range(1,6):  # 从指定的第一个值开始数，到达指定的第二个值后停止
#     print(value)  # 只输出1-5

# numbers = list(range(1, 11, 2))  # list将结果直接转化为列表，且可以指定步长
# print(numbers)

# squares = []
# for value in range(1,12,2):
#     squares.append(value**2)
# print(squares)
#
# ## 简单的数值统计
# print(min(squares))
# print(max(squares))
# print(sum(squares))
#
# ### 2.6.2 列表解析
# squares = [value**2 for value in range(1,12,2)]
# # 列表解析将for循环和创建新元素的代码合并到一起，前半段是表达式，后半段是for循环
# print(squares)

#### 2.7 使用列表中的一部分
### 2.7.1 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])  # 使用第一个元素的索引和最后一个元素索引加1，这里是输出前三个元素
#
# # 提取第2～4个元素
# print(players[1:4])

# # 如果没有指定第一个索引，将自动从列表开头开始
# print(players[:4])
#
# # 如果没有指定第二个索引，将自动到列表末尾的所有元素
# print(players[2:])
#
# print(players[-3:])  # 打印列表中最后三名队员的名字

### 2.7.2 遍历切片
# print('Here are the first three players on my team:')
# for player in players[:3]:
#     print("\t"+player.title())

### 2.7.3 复制列表
# friend_players = players[:]  # 这里省略了两个索引，代表对整个列表的复制。使用切片进行复制。
# print(friend_players)
# players.append('yao ming')
# friend_players.append('liu xiang')
# print(friend_players)
# print(players)
# 这里如果通过赋值直接复制列表，会出现不是将列表副本赋值给新变量，而实际上是将列表关联到新列表中，这样更改一个列表中的元素，另一个随之改变。

#### 2.8 元组
## 列表适合储存可能变化的数据集，而元组可储存一些不可修改的元素
dimensions = (200, 50)  # 元组是用圆括号来标识
print(dimensions[0])  # 访问和列表一样

# 虽然不能给修改元组元素，但是可以重新给元组赋值
dimensions = (400, 100)
print(dimensions[1])
