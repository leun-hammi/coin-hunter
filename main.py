import turtle
import random

island = turtle.Screen()
hunter = turtle.Turtle()
coin = turtle.Turtle()
score_place = turtle.Turtle()

island.bgpic("treasure-island.gif")
island.addshape("girl_left.gif")
island.addshape("girl_right.gif")
island.addshape("coin.gif")

score_place.penup()
score_place.speed(1000)
score_place.goto(220,280)
score_place.hideturtle()

hunter.penup()
hunter.speed(1000)
hunter.goto(0,-150)
hunter.shape("girl_right.gif")

def right():
    hunter.shape("girl_right.gif")
    hunter.setheading(0)
    hunter.forward(10)

def left():
    hunter.shape("girl_left.gif")
    hunter.setheading(180)
    hunter.forward(10)

turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")

turtle.listen()

coin.shape("coin.gif")
coin.penup()
coin.speed(1000)
coin.goto(-280,280)

def move():
    y = coin.ycor()
    coin.sety(y-3)
score = 0
score_place.write(f"score:{score}",font = ("Arial", 20, "bold"))
while True:
    island.update()
    move()
    if coin.ycor() < -280 :
        x = random.randint(-280,280)
        coin.goto(x,280)
    if coin.distance(hunter) < 50 :
        score_place.clear()
        score +=1
        score_place.write(f"score:{score}",font = ("Arial", 20, "bold"))
        x = random.randint(-280,280)
        coin.goto(x,280)

turtle.done()
