num1 = eval(input("Enter a number: "))
num2 = eval(input("Enter another number: "))


def add(num1, num2):
 print(num1+num2)


def sub(num, num2):
 print(num1-num2)


def mul(num1, num2):
 print(num1*num2)


def quot(num1, num2):
 print(num1/num2)


def rem(num1, num2):
 print(num1 % num2)


def fd(num1, num2):
 print(num1//num2)


def exp(num1, num2):
 print(num1**num2)


n = eval(input('Press 1 for addition, 2 from subtraction, 3 for multiplication, 4 for quotient, 5 for remainder, 6 for floor division, 7 for exponentiation: '))

if n == 1:
 add(num1, num2)
elif n == 2:
 sub(num1, num2)
elif n == 3:
 mul(num1, num2)
elif n == 4:
 quot(num1, num2)
elif n == 5:
 rem(num1, num2)
elif n == 6:
 fd(num1, num2)
else:
  exp(num1, num2)
