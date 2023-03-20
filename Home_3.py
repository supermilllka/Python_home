"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. Пользователь в первой строке вводит 
натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка 
содержит число X. Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count). 
Замерьте время работы двух алгоритмов и сравните, подумайте,почему оно отличается.
*Пример:*
5
    1 2 3 4 5
    3
    -> 1"""

input_list = [] 
count = 0
cnt = 0
import time
list_len = int(input("Введите кол-во эл. в списке: "))
for _ in range(list_len):
    input_list.append(int(input(f" Ввведите число: ")))
print(input_list)    
x = int(input("Введите число X: "))

count = input_list.count(x)
start = time.perf_counter()
print(f"Число {x} встречается {count} раз в массиве - 1 вариант")
end = time.perf_counter()
firsr_time = end - start


for i in input_list:
    if i == x:
        cnt += 1
start = time.perf_counter()        
print(f"Число {x} встречается {cnt} раз в массиве - 2 вариант")
end = time.perf_counter()
second_time = end - start
print(firsr_time/second_time)


"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой 
строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя 
строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""

input_list = [] 
list1 = []
list_len = int(input("Введите кол-во эл. в списке: "))
for _ in range(list_len):
    input_list.append(int(input(f" Ввведите число: ")))
print(input_list)    
x = int(input("Введите число X: "))
nearest_value = input_list[0]
for i in input_list:
    if abs(i-x) < abs(nearest_value - x):
        nearest_value = i 
print(nearest_value)