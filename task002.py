"""Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

Пример:
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9,0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]"""


from random import randint
list_1 = list(randint(-10, 11) for i in range(int(input("Введите кол-во элементов списка: "))))


def arr_idx (num_min, num_max, list_1):
    list_2 = []
    for i in range (len(list_1)):
        if list_1[i] >= num_min and list_1[i] <= num_max:
            list_2.append(i)
    return list_2
   

num_min = int(input("Введите минимальное значение диапазона: "))
num_max = int(input("Введите максимальное значение диапазона: "))


print(list_1)
print(arr_idx(num_min, num_max, list_1))

