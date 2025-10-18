print("1 for circle, 2 for rectangle, 3 for square")
a=int(input("choose one from 1 , 2 , 3: "))

if a==1:
    print("circle area calculation")
    r=float(input("Enter the radius:"))
    area=3.14*r**2
    print("area of circle is:", area)
elif a==2:
    print("rectangle area calculation")
    length=int(input("Enter length:"))
    breadth=int(input("Enter breadth:"))
    rectangle=length*breadth
    print("area of rectangle is:", rectangle)
elif a==3:
    print("square area calculation")
    side=int(input("Enter a number:"))
    square=side*side
    print("area of square is:", square)
else:
    print("you choose a wrong value")
