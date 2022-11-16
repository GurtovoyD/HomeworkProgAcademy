# 1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
# Наприклад, 1 - "Monday".

week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
day_week = int(input("What is a day today?"))
print(week.get(day_week, "I don't know this day of a week!!!"))

# 2. Опишіть кота (домашня тварина) на основі словника.
cat = {"Color": "Brown",
       "Breed": "Sphinks",
       "Weight": "10 kg",
       }
print(cat.values())

# 3.Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику,
# скільки разів яка літера зустрічається в цьому рядку.
# Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.
text = input()
letters = {}
for i in range(len(text)):
    if text[i] in letters:
        continue
    elif text[i].isalpha():
        letters[text[i]] = text.count(text[i])
print(letters)

# 4. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери,
# які є одночасно і в першому, і в другому рядку. Наприклад, для рядків «Hello» та «World» на екрані
# мають бути літери «l» та «o».'

txt = set(input("First sentence - ").replace(" ", ""))
txt1 = set(input("Second sentence - "))
print(txt & txt1)

# 5. Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.
# 6. Створіть список із числами, які є в обох списках.
import random

c = list(random.sample(range(300), 100))
multiples3 = set()
multiples5 = set()
for i in range(len(c)):
    if not c[i] % 3:
        multiples3.add(c[i])
    if not c[i] % 5:
        multiples5.add(c[i])
print(f'Кратні 3 - {multiples3}, \n'
      f'Кратні 5 - {multiples5}, \n'
      f'Спільні - {multiples5 & multiples3}')
