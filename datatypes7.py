input_string = input("Enter strings separated by comma ")
a_list = input_string.split(",")
longest_string = max(a_list, key=len)
print(longest_string)