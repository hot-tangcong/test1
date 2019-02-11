# Mixin
# 在今后框架学习中会大量用到Mixin
class Person():
    name = "LL"
    age =18
    def eat(self):
        print("EAT...")
    def drink(self):
        print("DRINK...")
    def sleep(self):
        print("SLEEP...")

class Teacher(Person):
    def work(self):
        print("WORK...")
class Student(Person):
    def study(self):
        print("STUDY...")

class Tutor(Teacher,Student):
    pass

t = Tutor()

print(Tutor.__mro__)
print("*" * 10)
print(t.__dict__)
print("*" * 10)
print(Tutor.__dict__)
print("*" * 10)

class TeacherMixin():
    def work(self):
        print("WORK...")
class StudentMixin():
    def study(self):
        print("STUDY...")
class TutorMixin(Person,TeacherMixin,StudentMixin):
    pass
tt = TutorMixin()
print(TutorMixin.__mro__)
print(tt.__dict__)
print(TutorMixin.__dict__)
