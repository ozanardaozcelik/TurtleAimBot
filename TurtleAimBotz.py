import turtle
import random
import time
import threading

screen = turtle.Screen()
screen.title("Kaplumbaga Oyunu")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(0)

score = 0
game_over = False
start_time = time.time()

board = turtle.Turtle()
board.hideturtle()
board.penup()
board.goto(0, 260)
board.write("Skor: 0", align="center", font=("Arial", 16, "bold"))

def update_score():
    board.clear()
    board.write(f"Skor: {score}", align="center", font=("Arial", 16, "bold"))

def move():
    if not game_over:
        x = random.randint(-380, 380)
        y = random.randint(-280, 280)
        t.goto(x, y)

def click(x, y):
    global score
    if not game_over:
        score += 1
        update_score()
        move()

t.onclick(click)

def timer():
    global game_over
    while True:
        if time.time() - start_time >= 30:
            game_over = True
            t.hideturtle()
            msg = turtle.Turtle()
            msg.hideturtle()
            msg.penup()
            msg.goto(0, 0)
            msg.write(f"Sure bitti! Skor: {score}", align="center", font=("Arial", 24, "bold"))
            break

move()
threading.Thread(target=timer).start()
screen.mainloop()