"""
                Лабораторная работа 3
    а) Построение графиков в полярных координатах (с помощью matplotlib)
"""
import matplotlib.pyplot as plt
import numpy as np

# rрo = 5 * cos (phi)
fig = plt.figure(figsize=(8, 6))  # Задаем размер поля

phi = np.linspace(0, 2 * np.pi, 100)  # Задаем диапазон от 0 до 4pi (100 точек)
rho = 2 * np.cos(phi) - 4/5 * np.tan(phi)  # Заданный график (ищем длину по формуле)

plt.polar(phi, rho)  # Строим график по точкам

plt.show()
