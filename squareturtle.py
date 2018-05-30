import turtle
t=turtle.Turtle()

def square(length, gak):
    for i in range(gak):
        t.fd(length)
        t.lt(360/gak)

square(200, 5)
