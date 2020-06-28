list1 = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    rng = int(input("Enter elements: "))
    list1.append(rng)
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
print("multiplying we get is:", multiplyList(list1))

