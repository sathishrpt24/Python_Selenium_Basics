class ClassExample:
    #not possible to create multiple constructor in python
    def __init__(self, **kwargs):
        self.a = A;
        self.b = B;
        self.c = 2;
        print("This is default constructor");
    def __init__(self,A,B,**kwargs):
        self.a = A;
        self.b = B;
        print("This is parameterised constructor");
    def class_function1(self):
        print("Printing the values of default constructor values assignment")
        print(self.a+" "+self.b);

    def class_function(self):
        print("Printing the values of parameterised constructor values assignment")
        print(self.a + " " + self.b);

#Obecject reference creation
#object1 = ClassExample();
object2 = ClassExample(A="Python",B="Tutorials");
object2.class_function()
object2.class_function1()