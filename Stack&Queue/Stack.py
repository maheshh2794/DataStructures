class Stack:
    def __init__(self,data):
        self.data = data
        # self.new = new

    def pushing(self,new):
        self.data.append(new)

    def poping(self,n):
        if n == None:
            self.data.pop()

    def display(self):
        print(self.data)


data =  Stack([11,2,3,45])
data.pushing(12)
data.poping(1)
data.pushing(22)
data.pushing(22)
data.display()