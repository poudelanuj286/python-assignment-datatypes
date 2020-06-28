def reaction(str1):
    nt = str1.find('not')
    pr = str1.find('poor')

    if pr > nt and nt > 0 and pr > 0:
        str1 = str1.replace(str1[nt:(pr + 4)], 'good')
        return str1
    else:
        return str1


print(reaction('The lyrics is not that poor!'))
print(reaction('The lyrics is poor!'))