# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Введите первый элемент ')) #первый элемент
d = int(input('Введите разность элементов ')) #разность элементов
n = int(input('Введите их количество ')) #количество

print(f"N-ый член прогресии: {a1+d*(n-1)}")