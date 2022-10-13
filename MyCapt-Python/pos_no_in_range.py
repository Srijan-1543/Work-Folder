list = []
output = []
n = int(input("Enter number of elements : "))
print("Enter the numbers:")
for i in range(0, n):
    ele = int(input())
    list.append(ele)
print("Input list: ", list)

for i in range(0, n):
  if list[i] > 0:
      output.append(list[i])

print("Output list: ", output)
