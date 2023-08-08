# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 1, 2, 5
# Вывод: 1, 3, 5, 7, 9

# first_el = int(input("Введите первый элемент ->"))
# step = int(input("Введите шаг ->"))
# list_len = int(input("Введите количество элементов -> "))
#
#
# def list_feeling(a1, l, d):
#     list_num = []
#     for i in range(1, l+1):
#         list_num.append(a1 + (i-1)*d)
#     return list_num
#
#
# print(list_feeling(first_el, list_len, step))


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3


list_len = int(input("Введите количество элементов -> "))
min_num = int(input("Введите нижнюю границу диапазона -> "))
max_num = int(input("Введите верхнюю границу диапазона -> "))
list_num = [int(input("Введите элемент списка ->")) for i in range(0, list_len)]
print(list_num)


def find_index(l, m, n):
    result = []
    for i in range(0, list_len):
        if m < list_num[i] < n:
            result.append(i)
    return result


print(find_index(list_num, min_num, max_num))
