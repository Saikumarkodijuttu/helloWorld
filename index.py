class A:
    def fun1(self):
        print("Child class")
class B(A):
    def fun2(self):
        print("Parent class")

obj = B()
obj.fun1()
obj.fun2()