# 多继承的例子
# 子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("I am swimming")

class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("I am flying")

class Person():
    def __init__(self,name):
        self.name = name
    def work(self):
        print("I am wokong")

class SuperMan(Person,Bird,Fish):
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name):
        self.name = name

# 多继承的例子
s = SuperMan("TT")
s.fly()
s.swim()

# 单继承的例子
stu = Student("cc")
stu.work()