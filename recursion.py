
import turtle
import random

colour = ['blue', 'dark blue', 'green', 'yellow']

def tree(branchLen,t):
    if branchLen > 5:
        t.color(random.choice(colour))
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-5,t)
        t.left(40)
        tree(branchLen-5,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(1000)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(55,t)
    myWin.exitonclick()

main()


             
    
