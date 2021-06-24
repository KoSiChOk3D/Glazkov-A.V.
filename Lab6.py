"""
                Лабораторная работа 6
    а) Напишите функцию, которая возвращает наибольший из трех целочисленных аргументов;

    б) Напишите функцию, которая имеет два аргумента int: нижний предел и верхний предел.
    Функция должна читать целое число из входных данных.
    Если это число выходит за указанные пределы, функция должна снова вывести меню (используя функцию из части а)),
    чтобы повторно предложить пользователю ввести новое значение.
    Если введенное целое значение попадает в рамки пределов, функция должна возвратить его в вызывающую функцию.
    Ввод нецелочисленного значения должен приводить к возвращению функцией значения,
    соответствующего выходу из программы
    (Часть а. Напишите функцию, которая выводит на экран меню из четырех пронумерованных вариантов
    и предлагает выбрать один из них. Ввод верхнего и нижнего предела, возможность изменить входящее
    целое число повторным вводом с клавиатуры и выход из меню и программы)

    в) Реализуйте сортировку массива вставками (массив из целых чисел)
"""

from os import system

# пункт а)
print("\t\tПункт 1")

nums = [int(i) for i in input("Введите 3 числа (через пробел): ").split()]
if len(nums) > 3:
    print("Чисел больше, чем 3")
    system(exit(0))
print(f"Большее число: {max(nums)}")


# пункт б)
print("\n\t\tПункт 2")

up, down = 0, 0
number = 0


def new_borders():
    while True:
        down = int(input("\nВведите нижний предел: "))
        up = int(input("Введите верхний предел: "))
        if up > down:
            return up, down
        print("Неверные границы!")


def new_number():
    while True:
        number = input("\nВведите целое число: ")
        if number.isdigit():
            return number
        print("Число не целое!")


def menu(up, down, number):
    while True:
        print("\nВыберите нужный пункт:\n"\
              "а) Ввод новых пределов;\n"\
              "б) Ввод нового числа;\n"\
              "в) Выход из меню;\n"\
              "г) Выход из программы;")
        answer = input("Выберите нужный вариант: ").lower()
        if len(answer) == 1:
            if answer == "а":
                up, down = new_borders()
            elif answer == "б":
                number = new_number()
            elif answer == "в":
                return up, down, number
            elif answer == "г":
                system(exit(0))
            else:
                print("\nЯ не знаю такого пункта\n")
        else:
            print("\nНеверный ввод!")


def range_checking(up, down):
    while True:
        try:
            if number == None:
                pass
        except:
            number = input("Введите число: ")

        if number.isdigit():
            number = int(number)
            if down <= number <= up:
                return number
            up, down, number = menu(up, down, number)
        else:
            print("Ошибка!")
            system(exit(0))


up, down = new_borders()
range_checking(up, down)


# пункт в)
print("\n\t\tПункт 3")


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
