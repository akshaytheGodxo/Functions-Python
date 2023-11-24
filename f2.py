
def areaofCircle(radius):
    pi = 3.14
    print("Area of circle is : " , pi*(radius**2))    
    
def circumference(radius):
    pi = 3.14
    print("Circumference is : ",2*pi*radius)
x = float(input("Enter the radius: "))

areaofCircle(x)
circumference(x)