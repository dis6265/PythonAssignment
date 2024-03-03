# 1. Write a python script to take your name as input from the user and then print it.
name=input("Enter your name :")
print(name)

# 2. Write a python script to take input from the user. Input must be a number.
num=int(input())
print(type(num))

# 3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("sum = ",a+b)

# 4. Write a python script which takes the radius from the user and display area of a circle.
rad=int(input("Enter radius for cal the area of circle :"))
print("Area of Circle with radius{} is {}".format(rad,3.14*rad*rad))

# 5. Write a python script to calculate the square of a number. Number is entered by the user.
s=int(input("Enter a number"))
print("Square of {} is {}".format(s,s*s))

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.
base=int(input("Enter base for cal area of tringle :"))
ht=int(input("Enter height for cal area of tringle :"))
print("Area of Tringle : {}".format(1/2*(base*ht)))

# 7. Write a python script to calculate average of three numbers, entered by the user
x=int(input("Enter first number"))
y=int(input("Enter second number"))
z=int(input("Enter third number"))
print("Average of {}, {} and {} is {}".format(x,y,z,(x+y+z)/3))

# 8. Write a python script to calculate simple interest
p=int(input("Enter the Priciple :"))
t=int(input("Enter time :"))
r=int(input("Enter rate :"))
print("Simple Interest = ",(p*r*t)/100)

# 9. Write a python script to calculate the volume of a cuboid.
l=int(input("Enter length of the cubic :"))
b=int(input("Enter breath   of the cubic :"))
h=int(input("Enter height  of the cubic :"))
print("Volume of a cuboid =",(l*b*h))

# 10. Write a python script to calculate area of a rectangle
len=int(input("Enter length of the rectangle :"))
wid=int(input("Enter width of the rectangle :"))
print("area of a rectangle =",(len*wid))