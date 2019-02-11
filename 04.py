class Teacher():
    name = "dana"
    age = 19

    def say(self):
        self.name = "yaona"
        self.age = 17
        print("My name is {0}".format(self.name))
        # 调用类的成员变量需要用__class__
        print("My name is {0}".format(__class__.age))
        print("My age is {0}".format(self.age))
    def sayAgain():
        print(__class__.name)
        print(__class__.age)
        print("hello world")
t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()
# 通过对象访问会报错
#t.sayAgain()
