#№1
n = int(input("Введите число: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")
#№2
rat = {
    'USD': {'EUR': 0.92, 'RUB': 110},
    'EUR': {'USD': 1/0.92, 'RUB': 119},
    'RUB': {'USD': 1/110, 'EUR': 1/119},
}

while True:
    fr = input("Из какой валюты (USD/EUR/RUB) или 'exit': ").upper()
    if fr == "EXIT":
        break
    to = input("В какую валюту (USD/EUR/RUB): ").upper()
    if fr not in rat or to not in rat[fr]:
        print("Неподдерживаемая конвертация")
        continue
    amo = float(input(f"Сумма в {fr}: "))
    print(f"{amo:.2f} {fr} = {amo * rat[fr][to]:.2f} {to}")

#№3
a = int(input("Нижняя граница: "))
b = int(input("Верхняя граница: "))
if a > b:
    a, b = b, a
x = int(input("Число из диапазона: "))
while not (a <= x <= b):
    x = int(input("Число вне диапазона. Введите снова: "))

out = []
for i in range(a, b + 1):
    out.append(f"!{i}!" if i == x else str(i))
print(" ".join(out))

#№4
import random

secret = random.randint(1, 500)
att = 0

while True:
    g = int(input("Ваше предположение (0 для выхода): "))
    if g == 0:
        print("Вы вышли из игры.")
        break
    att += 1
    if g < secret:
        print("Больше!")
    elif g > secret:
        print("Меньше!")
    else:
        print(f"Угадано! число {secret} за {att} попыток.")
        break
