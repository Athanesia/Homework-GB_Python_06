#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
 
lo, hi = 3, 8
data = [randint(1, 10) for _ in range(20)]
print("Заданный массив:", data, sep='\n')
indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
print("Индексы:", indexes, sep='\n')
result = []