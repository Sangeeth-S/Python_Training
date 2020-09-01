class Car_details:
    def __init__(self,name,color,model):
        self.name = name
        self.color = color
        self.model = model
    def my_function(self,company):
        print(self.name)
        print(self.color)
        print(self.model)
obj = Car_details("Benz" , "Red", "2020")
obj.my_function("Mercedes")
