class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        print("This is init function")



s1 = Student("John",100)
s2 = Student("Doe",200)
print(s1.name,s1.age)
print(s2.name,s2.age)
