# 继承中的构造函数 -2
class Animal():
    def __init__(self):
        print("Animal")

class Crawel(Animal):
    def __init__(self,name):
        print("Crawl Animal{0}".format(name))

class Dog(Crawel):
    def __init__(self):
        print("I am init in dog")

class Cat(Crawel):
    pass

# 实例化的时候，自动调用了Dog的构造函数，参数匹配，不报错
kk = Dog()

# 由于 Cat 没有构造函数，则向上查找
# 因为Crawel的构造函数需要两个参数，实例化的时候只给了一个，所以报错
c = Cat()
