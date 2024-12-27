#  Python Basics

print('hello')
a = 3
print(a)
str_1 = "welcome"
print(str_1)

b, c, d = 5,6.5,"Great"

print(b)
print(c)
print(d)

print("Hello",b)
print("Hello "+str_1)

# print("Hello"+b)

print("{} {} {} {}".format("Value are",b,"and",c))
name = "Priya"
age = 25

# python f-string
print(f"Name: {name}, Age: {age}")

# Python Datatypes
print(type(b))
print(type(c))
print(type(d))

values = [1,3,"piya",4,5]

print(values)
print(values[1])
print(values[-1])
print(values[-2])
print(values[1:3])

values.insert(3,"test")
print(values)

values.append("end")
print(values)

values[2] = "TEST"
print(values)

del values[0]
print(values)

# lists ,tuples and dictionaries

# tuple - same as LIST datatype but immutable
val = (1,2,"test",4.5)
print(val[1])
# val[2] = "hello"

dic = {"a":2,4:"bcd","c":"hello"}
print(dic[4])
print(dic["c"])

dict = {}
dict["firstName"] = "Rahul"
dict["lastName"] = "shetty"
dict["gender"] = "Male"
print(dict)
print(dict["lastName"])

# loops
greeting = "Morning"

if greeting == "Morning":
    print("condition matches")
    print("Second line")
else:
    print("Conditiion do not matches")

# for loop
obj = [2,3,4,5,6,7,8]
for i in obj:
    print(i*2)

print("-----------")
# range(i,j) -> i to j-1


sum = 0
for j in range(1,6):
    sum +=j
print(sum)

#  - normal for loop ; for(int i=0;i<6;i++)
# for j in range(1,6,2) - increment value is 2 here
for k in range(1,15,5):
    print(k)

#   while loops
i = 4
while i>1:
    if i!=3:
        print(i)
    i-=1

def greetMe(name):
    print("Good morning "+name)

def sum(a,b):
    return a+b

print(sum(3,6))

greetMe("piya")




