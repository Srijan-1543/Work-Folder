
test_str = input("Enter the string :")

res = {i: test_str.count(i) for i in set(test_str)}

# printing result
print("The count of all characters in String is :\n ", set(res))
