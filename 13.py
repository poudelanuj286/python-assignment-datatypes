input_string = input("Enter strings separated by comma ")
words = input_string.split(",")
# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)