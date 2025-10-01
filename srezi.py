# string = input()
# string1 = 'Hello World!'
# print(len(string1))
# print(string1*10)
# print(string + string1)
# print(string1[0])#h
#  #Срез
#  #String[a:b:c] - a = left index, b = right index, c = step
# print(string1[0:5]) #hello
# print(string1[0:10:2])
#  #find rfind
# print(string1.find('World')) #Index w, the search goes from left to right
# print(string1.find('l')) #The search goes from left to right
#  #replace - replaces a line with a new one
#  #replace(old, new)
# print("Date_1".replace("t", "TT"))
#  #Method count - counting occurrences (elements)
# print(string1.count('l')) #3
#  #Using lists
# primes = [2, 3, 5, 7, 11, 13]
# Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# print(type(primes)) #obj: list
# print(primes[0]) #2
# print(primes) # 2,3,5,7,11,13
# for i in primes:
#     print(i , end = ' ')
# print()
#  #Delete and adding a new element
# list_user = []
# from random import randint
# for i in range(10):
#     list_user.append(randint(0, 10)) #Added
# print(list_user)
# list_user.pop() #Delete a last symbol
# print(list_user)
#  #split and join
#  # 1 2 3
# str_val = input()
# str_list = str_val.split() # str_list = ['1', '2', '3']
#  #Specifying a parameter split - is a line separator
#  #Removes an element and creates a list
# for i in str_val:
#     if type(i) == int: #decimal(i)
#         str_list.append(i) #int(i)
# list_color = ['red', 'green', 'blue']
# print("+".join(list_color))
#
#  #List generators
#  #Fill the list randomly with only even numbers fo 10
#  #Way 1
# list_a = []
# while len(list_a) < 10:
#     a = randint(0, 10)
#     if a % 2 == 0:
#         list_a.append(a)
# print(list_a)
#
#  #Way 2
# list_b = [ i for i in range(10) if i % 2 == 0]
# print(list_b)
#  #list_c = [randint(1, 10) for i om range(10)
#
#  #Task 1
# list_u = []
# for i in range(10):
#     list.append(randint(0, 10))
# summ = 0
# for i in list_u:
#     summ += i
# print(f"List: {list_u}  \nSumm: {summ}")

 #Task 2
numbers = [5, 3, 8, -2, 7]

minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum:", minimum)

 #Task 3
numbers = [2, 3, 4, 5, 10, 11]
count = 0

for n in numbers:
    if n > 1:
        prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                prime = False
                break
        if prime:
            count += 1
print(count)

 #Task 4
numbers = [1, 2, 3, 2, 4, 2]
target = 2
count = 0
new_list = []

for num in numbers:
    if num == target:
        count += 1
    else:
        new_list.append(num)

print("New list:", new_list)
print("Deleted elements:", count)

 #Task 5
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
result = list_1 + list_2

print(result)

 #Task 6
numbers = [1, 2, 3, 4]
power = 3
new_list = []

for num in numbers:
    new_list.append(num ** power)

print("New list:", new_list)













