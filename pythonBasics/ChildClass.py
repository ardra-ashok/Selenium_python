from oopsDemo import Calculator


class ChildClass(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,5,8)

    def getChildData(self):
        return self.num2 +self.num +self.sum()

obj = ChildClass()
print(obj.getChildData())