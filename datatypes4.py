
def strings3(a, b):
  str1 = b[:2] + a[2:]
  str2 = a[:2] + b[2:]

  return str1 + ' ' + str2
st1= input("enter a string")
st2= input("enter another string")
print(strings3(st1, st2))