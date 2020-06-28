def strings4(st1):
  length = len(st1)

  if length > 2:
    if st1[-3:] == 'ing':
      st1 += 'ly'
    else:
      st1 += 'ing'

  return st1
abc = input("enter a string")
print(strings4(abc))
