from turtle import *
 
 
def start(x: float):
    """This function clears window and make turtle go to start"""
    clear()
    penup()
    x = x if x < 0 else -x
    goto(x, 0)
    pendown()
 
 
def curve_minkowski(length: float, iterations: int):
    """This function draw Minkowski's curve"""
 
    if iterations == 0:
        forward(length * 4)
    else:
        curve_minkowski(length/3, iterations - 1)
        left(90)
        curve_minkowski(length/3, iterations - 1)
        right(90)
        curve_minkowski(length/3, iterations - 1)
        right(90)
        curve_minkowski(length/3, iterations - 1)
        curve_minkowski(length/3, iterations - 1)
        left(90)
        curve_minkowski(length/3, iterations - 1)
        left(90)
        curve_minkowski(length/3, iterations - 1)
        right(90)
        curve_minkowski(length/3, iterations - 1)
 
 
LENGTH = 100       # длина линии
 
ITERATION = 1      # номер итерации
 
start(LENGTH * 2)
 
curve_minkowski(LENGTH, ITERATION)
 

exitonclick()    # функция чтобы программа не завершалась сразу

