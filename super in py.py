class Parent :
    var1="I am variable of class 1"
    def __init__(self):
        self.var1="I am instance variable of class 1"
        self.var2="I am second instance varible of class 1"
        self.super="Super"
class Child(Parent) :
    var2="I am varible of class 2"
    var1="I am variable of child class"
    def __init__(self):
        self.var1="I am instance varible of class 2"
        self.var2="I am second instance varible of class 2"
        super(Child, self).__init__()

A=Parent()
B=Child()
print(B.var2)