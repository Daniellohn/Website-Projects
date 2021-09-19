# An Aggie does not lie cheat or steal, nor tolerate those who do
# i did not receive any unauthorized aid on this assignment
# Daniel Lohn   UIN: 427004202  Section: 510   Date: 11/20/2018
import turtle

number_tally = int(input('what is the number of tallies?'))
counter = 0
my_turtle = turtle.Turtle()
my_turtle.right(90)
my_turtle.up()
my_turtle.back(200)
my_turtle.left(90)
my_turtle.back(300)
my_turtle.right(90)
my_turtle.down()
five_counter = 0


while counter < number_tally:
    if five_counter != 0 and five_counter % 5 == 0:
        def reorganize():
            '''This function makes a new row with a max tally count of 25'''
            my_turtle.up()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(500)
            my_turtle.left(90)
            my_turtle.down()
            help(reorganize)
        reorganize()
    if number_tally - counter < 5:
        my_turtle.forward(50)
        my_turtle.up()
        my_turtle.back(50)
        my_turtle.left(90)
        my_turtle.forward(20)
        my_turtle.right(90)
        my_turtle.down()
        counter = counter + 1
    if number_tally - counter >= 5:
        def tally():
            ''' This function creates a group of five tallies'''
            my_turtle.forward(50)
            my_turtle.up()
            my_turtle.back(50)
            my_turtle.left(90)
            my_turtle.forward(20)
            my_turtle.right(90)
            my_turtle.down()
            my_turtle.forward(50)
            my_turtle.up()
            my_turtle.back(50)
            my_turtle.left(90)
            my_turtle.forward(20)
            my_turtle.right(90)
            my_turtle.down()
            my_turtle.forward(50)
            my_turtle.up()
            my_turtle.back(50)
            my_turtle.left(90)
            my_turtle.forward(20)
            my_turtle.right(90)
            my_turtle.down()
            my_turtle.forward(50)
            my_turtle.up()
            my_turtle.back(50)
            my_turtle.left(90)
            my_turtle.back(80)
            my_turtle.right(30)
            my_turtle.down()
            my_turtle.forward(120)
            my_turtle.up()
            my_turtle.back(120)
            my_turtle.left(30)
            my_turtle.forward(120)
            my_turtle.right(90)
            my_turtle.down()
            help(tally)


        five_counter = five_counter + 1
        counter = counter + 5
        tally()




input()



