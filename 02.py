# 此案例说明
# 类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，
# 指向的是同一个变量

class A():
    name = "tc"
    age = 18
    # 注意say的写法，参数有一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200
# 此时，A称为类实例
print(A.name)
print(A.age)
print("*"*20)

print(id(A.name))
print(id(A.age))
print("*"*20)

a = A()
# 查看A内所有的属性
print(A.__dict__)
print(a.__dict__)
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print("*"*20)

a.name = "ttttt"
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print(A.__dict__)
print(a.__dict__)
