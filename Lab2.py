"""
                Лабораторная работа 2
    а) Создайте функцию, которая организует простейшей сжатие
    входящей символьной строки произвольного масштаба.
    Сжатие происходит по следующему принципу:
    если в строке есть последовательность повторяющихся символов,
    то она заменяется на пару код символа и количество его повтора
    в строчке. Обеспечьте возможность ввода строки с клавиатуры.

    б) Реализуйте сортировку массива вставками. (массив из целых чисел).

    в) Создайте программу, позволяющую находить в строке подстроку и заменять её
    на другую произвольную подстроку в каждом месте обнаружения.
"""

# пункт а)
print("\t\tПункт 1")

string1 = input("Введите строку: ")
string2 = string1
string1 += " "
count = 1
i = 0
while i < len(string1) - 1:
    if string1[i] == string1[i+1]:
        if count == 1:
            char = string1[i]
        count += 1
    else:
        if count > 1:
            string2 = string2.replace(char*count, f"({ord(char)}, {count})", 1)
            char = ""
            count = 1
    i += 1

print(string2)


# пункт б)
print("\n\t\tПункт 2")

from random import randint


def insertion_sort(array):
    for i in range(len(array)):
        temp = array[i]
        pos = i

        while pos > 0 and array[pos - 1] > temp:
            # Меняем местами число, продвигая по списку
            array[pos] = array[pos - 1]
            pos -= 1
        array[pos] = temp

    return array


mas = [randint(0, 100) for _ in range(10)]  # Массив рандомных чисел от 0 до 99
print(", ".join(map(str, mas)))

mas = insertion_sort(mas)
print(", ".join(map(str, mas)))


# пункт в)
print("\n\t\tПункт 3")

string = input("Введите строку: ")
und_string1 = input("Введите подстроку, которую хотите заменить: ")
und_string2 = input("Введите подстроку, на которую хотите заменить: ")

string = string.replace(und_string1, und_string2)
print(string)
