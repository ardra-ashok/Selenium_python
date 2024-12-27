
ItemsIncart = 0;


if ItemsIncart != 2:
    raise Exception("Product cart count not matching!")

# assertion
assert(ItemsIncart == 2)

try:
    with open('test.txt', 'r') as reader:
        reader.read()
# except:
#     print("There is failure in try block")

except Exception as e:
    print(e)

finally:
    print("test finally")