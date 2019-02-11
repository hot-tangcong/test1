class Person():
    # name 是公有成员
    name = "tt"
    # __age是私有成员
    __age = 18

p = Person()
# name是公有变量
print(p.name)

# __age是私有变量
# 注意报错信息
print(p.__age)

# name mangling技术
print(Person.__dict__)

p._Person__age = 19
print(p._Person__age)