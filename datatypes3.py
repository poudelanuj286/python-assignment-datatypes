def strings2(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

abc = input("enter a string")
print(strings2(abc))