"""
                Лабораторная работа 1
    а) Написать программу, которая заменяет все четные числа
    в целочисленном статическом массиве на 0. (массив из 10 элементов)

    б) Ввод символа с клавиатуры (с проверкой что это именно символ),
    ввод строки с клавиатуры (с проверкой что это именно строка).
    Вывод в консоль номера, который символ занимает в строке, если он там есть.
    Если нет — вывод сообщения об отсутствии символа.

    в) Расчет определителя матрицы, матрица размером 3 на 3. Ввод чисел построчно. Числа только целые.
"""

from random import randint
from os import system

# пункт а)
print("\t\tПункт 1")

mas = [randint(0, 100) for _ in range(10)]  # Массив рандомных чисел от 0 до 99
print(", ".join(map(str, mas)))

for i in range(10):
    if mas[i] % 2 == 0:
        mas[i] = 0

print(", ".join(map(str, mas)))


# пункт б)
print("\n\t\tПункт 2")

while True:
    char = input("Введите символ: ")
    if len(char) == 1:  # Проверка на символ
        break
    print("Это не символ!")

while True:
    string = input("Введите строку: ")
    if len(string) > 1:  # Проверка на строку
        break
    print("Это не строка!")

pos = string.find(char)
if pos >= 0:
    print(f"Символ на {pos} позиции (считая с нуля).")
else:
    print("Данного символа нет в строке.")


# пункт в)
print("\n\t\tПункт 3")

matrix = [[0] * 3 for _ in range(3)]   # Инициализируем матрицу

for i in range(3):
    for j in range(3):
        while True:
            matrix[i][j] = input(f"matrix[{i}][{j}] -> ")
            if matrix[i][j].isdigit():
                matrix[i][j] = int(matrix[i][j])
                break
            print("Это не целое число!")

print("\n\t Матрица")
for i in range(3):
    for j in range(3):
        print(f"\t{matrix[i][j]}", end=" ")
    print()

determinant = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
               matrix[1][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
               matrix[2][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

print(f"Определитель: {determinant}")
