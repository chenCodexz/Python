# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def __init__(self, name, color):
       self.name = name
       self.color = color
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1=Vehicle("Fer","red")
car1.kind="convertible"
car1.value=60000.00
car2=Vehicle("Jump","blue")
car2.kind="van"
car2.value=10000.00
# test code
print(car1.description())
print(car2.description())