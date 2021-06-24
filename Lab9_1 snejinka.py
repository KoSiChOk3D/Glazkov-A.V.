import turtle           
import time

def koch_line(size, n):
  if n == 0:        # рисуем линию и дальше не идем
    t.fd(size)
    return
    
  a = size/3        # иначе разбиваем отрезок 
                    # и вместо него делаем набор отрезков  
  koch_line(a, n-1)
  t.left(60)
  koch_line(a, n-1)
  t.right(120)
  koch_line(a, n-1)
  t.left(60)
  koch_line(a, n-1)
                    # конец функции

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

t.color('black')
koch_line(350, 3)

turtle.done()   
