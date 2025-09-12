# # Циклы
# for i in range(0, 10):
#       print("*", end=' ')
#
# # Задание 1
#
# chis1 = int(input("Введите число в диапазоне от 1 до 100: "))
# if chis1 < 1 or chis1 > 100:
#     print("Ошибка")
# else:
#     if chis1 % 3 == 0 and chis1 % 5 == 0:
#         print("Fizz Buzz")
#     elif chis1 % 3 == 0:
#         print("Fizz")
#     elif chis1 % 5 ==0:
#         print("Buzz")
#     else:
#         print(chis1)
#
# # Задание 2
#
# v = int(input("Введите число которое хотите возвести в степень: "))
# s = int(input("Выберите и впишите степень, от 0 до 7: "))
# if s == 0:
#     print("Ответ:", v ** 0)
# else:
#     if s == 1:
#         print("Ответ:", v ** 1)
#     else:
#         if s == 2:
#             print("Ответ:", v ** 2)
#         else:
#             if s == 3:
#                 print("Ответ:", v ** 3)
#             else:
#                 if s == 4:
#                     print("Ответ:", v ** 4)
#                 else:
#                     if s == 5:
#                         print("Ответ:", v ** 5)
#                     else:
#                         if s == 6:
#                             print("Ответ:", v ** 6)
#                         else:
#                             if s == 7:
#                                 print("Ответ:", v ** 7)
#                             else:
#                                 print("Я не могу возвести в такую степень")
#
# # Задание 3

Sum = int(input("Введите сумму минут которую хотите потратить на разговор: "))
M = input("Доступные операторы:\nТеле2\nБилайн\nМтс\nЙота\nВведите оператор собеседника: ")

if M == 'Теле2':
    print('Стоимость разговора составит:', Sum * 2)
else:
    if M == 'Билайн':
        print('Стоимость разговора составит:', Sum * 1.7)
    else:
        if M == 'Мтс':
            print('Стоимость разговора составит:', Sum * 1.4)
        else:
            if M == 'Йота':
                print('Стоимость разговора составит:', Sum * 0.9)
            else:
                print("Неизвестный оператор!")

# Задание 4

def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        return base_salary + sales * 0.03
    elif sales <= 1000:
        return base_salary + sales * 0.05
    else:
        return base_salary + sales * 0.08

sales = []
for i in range(3):
    sales_amount = float(input(f"Введите объем продаж для менеджера {i+1}: "))
    sales.append(sales_amount)

salaries = [calculate_salary(s) for s in sales]

best_manager_index = salaries.index(max(salaries))
best_manager_salary = salaries[best_manager_index] + 200
best_manager_sales = sales[best_manager_index]

print("\n--- Итоги ---")
for i, salary in enumerate(salaries):
    print(f"Зарплата менеджера {i+1}: {salary:.2f}$")

print(f"\nЛучший менеджер: {best_manager_index + 1} (продажи: {best_manager_sales:.2f}$)")
print(f"Зарплата лучшего менеджера (с премией): {best_manager_salary:.2f}$")
