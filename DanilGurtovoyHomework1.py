# Exercise 1
print("Hello world")


# Exercise 2
print("Hello", "my", "world", sep="\n")

# Exercise 3
width = int(input("Input width of a rectangle - "))
length = int(input("Input length of a rectangle - "))
print("The area of the rectangle is " + str(width*length))

# Exercise 4
first_number = int(input("Input first number - "))
second_number = int(input("Input first number - "))
print(first_number - second_number, first_number + second_number,
      first_number / second_number, first_number * second_number, sep="\n")

# Exercise 5
radius = int(input("Input radius if a circle - "))
P = 3.14159
print(("The circle diameter = " + str((radius * 2)**2)), ("Circumference = " + str(P * radius * 2)),
      ("Area = " + str((P*radius)**2)), sep="\n")
