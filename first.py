# class car:
#     pass

# car1=car()
# car2=car()
# car3=car()

# car1.name="benz"
# car1.model="s500"
# car1.coler="black"
# car1.motor="petrol"
# #----------------------------------------------------------------
# #crate object bmw 
# car2.name="BMW"
# car2.model="Z4"
# car2.coler="orang"
# car2.motor="petrol"
# #------------------------------------------------------------------
# car3.name="sipa"
# car3.model="pride"
# car3.coler="wh"
# car3.motor="petrol"
# #-------------------------------------------------------------------

# print(car1.name,car2.name,car3.name)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


# ساخت یک شیء از کلاس Rectangle
my_rectangle = Rectangle(5,10)

# فراخوانی متد calculate_area بر روی شیء
area = my_rectangle.calculate_area()

print("مساحت مستطیل:", area)