# 1.
def txt(a, b, c):
    return f"{a + b}{c}"


# 2.
def per(lenght, weight):
    star = "*" * lenght
    return f"{star}\n" + f"*{' ' * (lenght - 2)}*\n" * (weight - 2) + f"{star}"

print(per(int(input("Lenght=")), int(input("weight="))))

# 3.
def func(item, ilist):
    if item in ilist:
        return ilist.index(item), item
    else:
        return -1
item = input("Введіть ваш номер - ")
ilist = list(input("List of numbers").replace(",","").split())

print(func(item, ilist))

# 4.
def text(a):
    b = "".join(a).split()
    return len(b)
print(text(input()))


# 5.
from num2words import num2words

def numbers(a):
    return num2words(a, to='currency').replace("euro", "dollars")

print(numbers(input()))

# 6.
def ryms(roman):
    rym_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    values = [rym_number[i] for i in roman]
    for i in range(len(values) - 1):
        if values[i] < values[i + 1]:
            values[i] *= -1
    return sum(values)


print(ryms("XXXIV"))
