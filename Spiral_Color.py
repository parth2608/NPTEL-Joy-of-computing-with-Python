import turtle
import random
turtle.bgcolor('black')
tur = turtle.Turtle()

width = 5
height = 7
dot_distance = 25

tur.penup()
list_color = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'pink', 'grey', 'brown']

tur.setpos(-250, 250)


def spiral(m, n):
    k = 0
    l = 0
    f = 0
    col = random.randint(0, 10)
    tur.color(list_color[col])
    tur.color('white')
    while k < m and l < n:
        if f == 1:
            tur.right(90)
        for i in range(l, n):
            tur.dot()
            tur.forward(dot_distance)
        k = k+1
        f = 1
        tur.right(90)
        col = random.randint(0, 10)
        tur.color(list_color[col])
        for i in range(k, m):
            tur.dot()
            tur.forward(dot_distance)
        n = n-1
        tur.right(90)
        col = random.randint(0, 10)
        tur.color(list_color[col])
        if k < m:
            for i in range(n-1, l-1, -1):
                tur.dot()
                tur.forward(dot_distance)
            m = m-1
            tur.right(90)
            col = random.randint(0, 10)
            tur.color(list_color[col])
        if l < n:
            for i in range(m-1, k-1, -1):
                tur.dot()
                tur.forward(dot_distance)
            l = l+1


spiral(20, 20)
turtle.done()