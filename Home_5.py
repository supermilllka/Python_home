"""Задача 6.
Дана строка (возможно, пустая), состоящая из букв
A-Z:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
BBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида:
A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения:
Если символ встречается 1 раз , он остается без изменений;
Если символ повторяется более 1 раза , к нему добавляется количество повторений"""

import re

def rle(str):
        result = []
        #str += ''
        count = 0
       
        for i in range(len(str)):
            count+=1
            #if (i+1) == len(str) or str[i] != str[i+1]:
            if i+1 == len(str) or str[i] != str[i+1]:
                result.append(f'{count, str[i]}')
                count = 0
        #print(*result, sep='')
        return result

string_list = str(input("Введите строку, состоящую из букв A-Z: "))
if len(string_list) > 0 and re.search(r'[A-Z]', string_list): 
        res = rle(string_list)
        print(*res, sep='')
else:
      print("Введены некорректные данные")