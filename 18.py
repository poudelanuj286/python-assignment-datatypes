list1 = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    rng = int(input("Enter elements: "))
    list1.append(rng)

print("Largest element is:", max(list1))
