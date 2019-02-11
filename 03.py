class Student():
    name = "tc"
    age = 18
    # 注意say的写法，参数有一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
    def say(s):
        s.name = "aaaa"
        s.age = 200
        print("My name is {0}".format(s.name))
        print("My age is {0}".format(s.age))

YY = Student()
YY.say()