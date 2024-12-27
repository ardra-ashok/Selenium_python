# read the file and store all the lines in list
#  reverse the list
with open('testReadWrite.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('testReadWrite.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)


