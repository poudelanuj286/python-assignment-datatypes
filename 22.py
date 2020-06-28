
def Remove(duplicate):
    flist1 = []
    for num in duplicate:
        if num not in flist1:
            flist1.append(num)
    return flist1

num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    list1 = []
    rng = int(input("Enter elements: "))
    list1.append(rng)
print("after removal of duplicates:", Remove(list1))