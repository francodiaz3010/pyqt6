import turtle

# Configurar la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear una instancia de Turtle
corazon = turtle.Turtle()
corazon.shape("turtle")
corazon.color("red")
corazon.speed(1)

# Dibujar el corazón
corazon.begin_fill()
corazon.fillcolor("red")
corazon.left(140)
corazon.forward(224)
for _ in range(200):
    corazon.right(1)
    corazon.forward(2)
corazon.left(120)
for _ in range(200):
    corazon.right(1)
    corazon.forward(2)
corazon.forward(224)
corazon.end_fill()

screen.exitonclick()