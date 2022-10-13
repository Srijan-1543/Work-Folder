n = int(input("Input n to print the fibonacci series upto the nth term (n>0): "))
x = 0
y = 1
list = []
list.append(x)
list.append(y)

if n <= 0:
    print("Incorrect")
elif n == 1:
    print(list[0])
elif n == 2:
    print(list)
else:
    z = 0
    for i in range(0, n-2):
        z = list[i] + list[i+1]
        list.append(z)
    print(list)
