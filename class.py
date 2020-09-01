class Student:
    def __init__(self,name,age,mobile):
        self.name = name      
        self.age = age
        self.mobile = mobile 
    def function(self):
        print("My name is " + self.name)
        print("My age is " + self.age)
        print("My mobile is " + self.mobile)
obj1 = Student("sangeeth", "23","36547555")
obj2 = Student("vijay", "25","3655552555")
obj3 = Student("vijay", "25","3655552555")
obj1.function()
obj2.function()
obj3.function() 