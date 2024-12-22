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




