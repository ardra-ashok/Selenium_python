file = open('testReadWrite.txt')

# read all the contents of file
print(file.read())

# only few chars
print(file.read(5))

# readline
print(file.readline())
print(file.readline())

# Read line by line using a method from a file
line = file.readline()
while line!="":
    print(line)
    line = file.readline()

for line in file.readlines():
    print(line)

file.close()

