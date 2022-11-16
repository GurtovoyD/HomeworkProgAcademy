# 1. Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту.

print(input("How are you?").lower().count("b"))

# 2. Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки введеного ім'я на валідність
# (мається на увазі, що, наприклад, в імені людини не може бути цифр, воно повинно починатися з великої літери,
# за якою повинні йти маленькі)
name = input()
print(name) if name.isalpha() and name.istitle() else print("False")

# 3. Напишіть програму, яка обчислить суму всіх кодів символів рядка.
code = input()
counte = 0
for i in range(len(code)):
    counte += ord(code[i])
print(counte)

# 4. Виведіть на екран 10 рядків із значенням числа Pi.
# У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.
import math
for i in range(2, 12):
    print(f"{math.pi:.{i}f}")


# 5. Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.
lenght = list(input().split())
print(max(lenght, key=len))


# Додаткові задачі до домашнього завдання:
# 1. Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери).
# Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту. Напишіть програму,
# яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"

stp = """
words = input()
"""
import timeit
s = """
for i in range(len(words)):
    if words.count(words[0]) == len(words):
        print(words[0])
        break
    elif words[:i] == words[i:i*2] and words[:i*2] == words[i*2:i*4]:
        if i:
            print(f"Vovochka wrote - {words[:i]}")
            break
"""
print(timeit.timeit(s, setup=stp, number=1000))

# 2. Напишіть програму для очищення тексту від HTML-тегів. Більше про html-теги https://html5book.ru/html-tags/
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, а другий закриває.
# - тег у собі може містити купу додаткової інформації.
# Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">

html = """
<!DOCTYPE html>
<script src="/link-fixup.js" defer></script>
<title>404 Not Found</title>
<style>
 body.loading div.failed, body.failed div.loading, div.failed { display: none; }
 body.loading div.loading, body.failed div.failed, div.loading { display: block; }
</style>
<body onload="document.body.className = 'failed'">
<script>document.body.className = 'loading'</script>
<div class="loading">
 <p>Loading...</p>
</div>
<div class="failed">
 <h1>Not Found</h1>
 <p>The page you are looking for is no longer available at this URL.</p>
 <p>Links to the multipage version of the specification are
 unfortunately likely to break over time. You might be able to find
 what you want from <a href="/multipage/">the contents page</a>.</p>
 <p>If you have found a broken link on the WHATWG site itself, please
 <a href="https://github.com/whatwg/html/issues/new">file an issue</a>.
 If you found a broken link from another site pointing to the WHATWG site,
 please let that site know of the problem instead. Thanks!</p>
</div>
"""

while "<" in html:
    start = html.find("<")
    stop = html.find(">")
    html = html.replace(html[start: stop + 1], "")
print(html)