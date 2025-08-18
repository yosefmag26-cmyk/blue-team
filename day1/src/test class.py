class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display__info(self):
                 
        print (f"{self.name}")
        print(f"{self.age}")
        print(f"{self.city}")              
p1=Person("Yosef",34,"masrata")
p1.display__info()           