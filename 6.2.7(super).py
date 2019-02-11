class A():
    pass
class B(A):
    pass
class C(B,A):
    pass
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)