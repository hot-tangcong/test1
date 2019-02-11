# 在python中，任何类都有一个共同的父类叫object
class Person():
    name = "None"
    age = 0
    __score = 0 # 考试成绩是秘密，只能自己知道，private
    _petname = "sec"    # 小名，protected，子类可以用，但不能公有
    def sleep(self):
        print("Sleeping...")
    def work(self):
        print("Make money")


# 父类写在括号内
class Teacher(Person):
    teacher_id = "111"
    name = "tttt"
    def make_test(self):
        print("attention")
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        Person.work(self)   # self是Teacher，子类可以“冒充”父类（父类不可以冒充子类）

        # 扩充父类的另一种方法
        # super代表得到父类
        super().work()
        self.make_test()

t = Teacher()
t.work()
print(t.name)
print(Teacher.name)
