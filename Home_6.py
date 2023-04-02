"""Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""


def arithmetic_progression(fir, dif, count):
    result = []
    #result.append(input_first_element)
    for i in range(1, input_count + 1):
        elem = input_first_element + (i - 1) * input_difference
        #print(elem)
        result.append(elem)
    return result

input_first_element = int(input("Введите первый элемент: "))
input_difference = int(input("Введите разность: "))
input_count = int(input("Введите количество элементов: "))


print(arithmetic_progression(input_first_element, input_difference, input_count))


"""Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)"""

import random

def find_index(arr, min, max):
    res = []
    for i in range(len(arr)):
        if arr[i] >= min and arr[i] <= max:
            res.append(i)    
    return(res)

array = [random.randint(1,20) for _ in range(10)]
print(array)
input_min = int(input("Введите min: "))
input_max = int(input("Введите max: "))

print(find_index(array, input_min, input_max ))
