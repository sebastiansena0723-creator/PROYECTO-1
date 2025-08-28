import turtle
ventana = turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")
t.color("pink")
t.speed(100)
 
for i in range(8):
    t.circle(100)
    t.left(45)
    t.write("flor", font=("arial",30, "normal"))   

    turtle.done