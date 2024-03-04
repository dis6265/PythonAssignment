# # 1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
# n=int(input("enter a number :"))
# print("{} number without last digit is {}".format(n,int(n/10)))

# # 2. Write a python script to get the last digit from a given number. (for example, if user
# # enters 2089 then your output should be 9)

# print("Last digit is {} of number {}".format(n%10,n))

# # 3. Write a python script to swap data of two variables
# a=int(input("enter value of a :"))
# b=int(input("enter value of b :"))
# print("Value of a ={} and b={}".format(a,b))
# temp=a
# a=b
# b=temp
# print("Value of a ={} and b={}".format(a,b))

# 4. Write a python script to find x power y, where values of x and y are given by user.
x=int(input("enter value of x :"))
y=int(input("enter value of y :"))
print("{} to the power of {} is {}".format(x,y,x**y))

# 5. Write a python script which takes a three digit number from the user and displays only its first digit.
d=int(input("Enter three digit number :"))
print("First digit of the number {} is {}".format(d,int(d/100)))

# 6. Write a python script which takes a three digit number from the user and displays only its middle digit.
rem=int(d/10)
print("First digit of the number {} is {}".format(d,rem%10))

# 7. Write a python script which takes a three digit number from the user and displays only its last digit.
print("First digit of the number {} is {}".format(d,int(d%10)))

# 8. Write a python script to use IN operator to display the data present in the list
lst=[10,20,12,30,35,75]
a=int(input("Enter a number :"))
print("{}".format(a in lst))

# 9. Write a python script to use NOT IN operator to display the data not present in list
print("{}".format(a in lst))

# 10. Write a python script to use IS operator to display if both variables are the same object or not?
print(x is y)