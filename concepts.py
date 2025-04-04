class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return super().method() + " B"

class C(B):
    def method(self):
        return super().method() + " C"

obj = C()
print(obj.method())

class X:
    pass

class Y:
    pass

class Z(X, Y):
    pass

print(Z.__mro__)

class Parent:
    x = 10

class Child(Parent):
    pass

obj = Child()
obj.x = 20
print(Parent.x, obj.x)