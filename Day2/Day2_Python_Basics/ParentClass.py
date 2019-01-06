class ParentClass:
    def __init__(self,A):
        self.a =A;
        print("This is Class A constructor");
    def function1(self):
        print("Class A - Function-1"+self.a)
    def function2(self):
        print("Class A - Function-2")
    def function3(self):
        print("Class A - Function-3")
    def function4(self):
        print("Class A - Function-4")

class Child(ParentClass):
    def __init__(self):
        print("child class constructor")
        ParentClass.__init__(self,"Sathish");
    def function1(self):
        print("child class- function-1");
        self.fun

    def function2(self):
        print("child class - function-2");

ref = Child();
ref.function1();
ref.function2();
ref.function3();
ref.function4();
#ref.
