# 1. Write a python script to add comments and print “Learning Python” on screen.
print("Learning Python")


# 2. Write a python script to add multi line comments and print values of four variables,each in a new line. Variable contains any values.
a=1
b="disha Patil"
c=88.4


# 3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
b=35
c=True
a="disha"
d=5.56
e=3+4j
print(type(b))
print(type(c))
print(type(a))
print(type(d))
print(type(e))

# 4. Write a python script to print the id of two variables containing the same integer values.
x=2
y=2
print("id of a {} an did of b ={}".format(id(x),id(y)) )

# 5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable
print(type(b),id(b))
print(type(c),id(c))
print(type(a),id(a))
print(type(d),id(d))
print(type(e),id(e))

# 6. Write a python script to print all the keywords
import keyword
print(keyword.kwlist)


# 7. On Python shell use help() function and display the list of keywords


# 8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. Write a python script to import A1 
# module in A0 and print value of the variable created in A0.py
#A0 and A1


# 9. Name the keywords, used as data in the Python script.
#True and False


# 10. Write a python script to display the current date and time. First create variables to
# store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)
from datetime import date, time
print(date.today())
t=time.isoformatstrftime(" %H : %M : %S")
print(t)