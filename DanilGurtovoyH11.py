class Products:
    def __init__(self, product: dict):
        self.product = product

    def __str__(self):
        for key, value in self.product.items():
            print(key, value)
        return "--------------------\nФормат: Назва тварини Кількість Вартість\n--------------------"


class Basket():

    def __init__(self, product1):
        self.product1 = product1

    def __str__(self):
        print("Ваше замовлення: \n Найменування:     Кількість:       Ціна:")
        for key in self.product1:
            print(
                f"{key}    {self.product1[key]['Count']}     {self.product1[key]['Count'] * self.product1[key]['Cost']}")
        return "Дякуємо за покупку!"


class User:

    def __init__(self, name, surname, mobile):
        self.name = name
        self.surname = surname
        self.mobile = mobile

    def __str__(self):
        return f"\n\n\n\n\nІм'я - {self.name}, прізвище - {self.surname}, номер телефону - {self.mobile}"


product_dict = Products({"Parrot": 50, "Cat": 100, "Dog": 80, "Tiger": 1000, "Mouse": 60, "Carrot": 80})
print("Впишіть кого саме ви хочете купити і в якій кількості!"
      "\n Щоб закінчити - введіть слово 'СТОП'")
print(product_dict)

basket_user = {}
while True:
    animals, count, cost = map(str, input().split())
    if animals.lower().find("stop" or "стоп") >= 0:
        break
    else:
        basket_user[animals] = {"Count": int(count), "Cost": int(cost)}

basket_user = Basket(basket_user)
print("Ваш заказ майже сформований! \n Тепер введіть ваші дані в форматі:")
user_info = User(input("Ваше ім'я - "), input("Ваше прізвище - "), input("Ваш номер телефону - "))
print(user_info)
print(basket_user)
