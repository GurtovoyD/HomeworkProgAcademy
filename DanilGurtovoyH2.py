# Exercise 1
a = "123"
print(int(a))

# Exercise 2
b = 123
print(float(b))

# Exercise 3
c = 12.345
print(int(c))

# Exercise 4
card_number = (input("Input card number - ").replace(" ", ""))
print(card_number[-4:])

# Exercise 5
number = input("A three-digit number - ")
print(int(number[0]) + int(number[1]) + int(number[2]))

# Exercise 6
side1= int(input("Input first side of triangle - "))
side2= int(input("Input second side of triangle - "))
side3= int(input("Input third side of triangle - "))
p = (side1 + side3 + side2) / 2
print((p*(p - side1) * (p - side2) * (p - side3))**0.5)

# Exercise 7
number7 = input("Please, input your number - ")
sum = 0
for i in number7:
    sum+=int(i)
print(sum)

# Exercise 8
number8 = (input("Please, input your number - ").replace(" ", ""))
print(len(number8))

# Exercise 9
number9 = (input("Please, input your number - ").replace(" ", ""))
print(number9[-1::-1])