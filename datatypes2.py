

def strings1(str):
  if len(str) < 2:
    return 'Empty String'

  return str[0:2] + str[-2:]
abc = input("enter a string")
print(strings1(abc))