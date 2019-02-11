# 继承中的构造函数 -3
class Animal():
    def __init__(self):
        print("Animal")

class Crawel(Animal):
    pass

class Dog(Crawel):
   pass

class Cat(Crawel):
    pass

kk = Dog()
c = Cat()
