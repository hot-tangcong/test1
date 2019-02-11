# 继承中的构造函数
class Animal():
    def __init__(self):
        print("Animal")

class Crawel(Animal):
    def __init__(self):
        print("Crawel")

class Dog(Crawel):
    def __init__(self):
        print("I am init in dog")

# 猫没有构造函数
class Cat(Crawel):
    pass
# 实例化的时候，自动调用了Dog的构造函数
kk = Dog()

# 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类的构造函数
# 在Crawel中查找到了构造函数，则停止向上查找
c = Cat()