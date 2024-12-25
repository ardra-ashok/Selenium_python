class Calculator:
    num = 100

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("test default constructor")

    def getData(self):
        print("test method")

    def sum(self):
        return self.a +self.b

obj = Calculator(2,3)
print(obj.sum())
obj.getData()
print(obj.num)

print("-----------------------")

obj = Calculator(3,4)
print(obj.sum())
obj.getData()
print(obj.num)

