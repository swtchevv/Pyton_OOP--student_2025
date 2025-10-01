'''
arr = [a, b, c] - список

x.append() - добавляет в конец списка

x.insert() - добавляет внутрь списка

x.pop() - удаляет из конца списка
'''

from time import time

start = time()
arr = []
for _ in range(100_000_000):
    arr.append(5)
stop = time()
print(stop - start)















