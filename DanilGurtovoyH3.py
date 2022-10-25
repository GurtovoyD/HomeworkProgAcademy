# Exercise 1
a = int(input("Input number - "))
ref = a < 0 and a
print(ref)


# Exercise 2
b = int(input("Input number - "))
ref = b < 20
print(ref)

# Exercise 3
c = int(input("Input number - "))
ref = c == 0
print(ref)

# Exercise 4
d = int(input("Input number - "))
ref = d % 2 == 0 and f"Even {d}" or d % 2 == 1 and f"Odd {d}"
print(ref)

# Exercise 5
a, b, c = map(int, input("Input 3 numbers - ").split())
ref = a <= b and a <= c and f"The less number is {a}" or b <= a and b <= c and f"The less number is {b}" or \
      c <= b and c <= a and f"The less number is {c}"
print(ref)
