# This file was created by Bradley Kemp on 9/21/23:
# Final Submission for RPS

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
Have the game solely within PyGame, not the terminal
Have the computer select one and display it
'''

# Import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint

# Setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# Setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

# Define the width and height for each item:

rock_w = 256
rock_h = 280

scissors_w = 256
scissors_h = 170

paper_w = 256
paper_h = 204

# Assigns an input to the variable player_choice
player_choice = ""

cpu_choice = ""

# Setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
# Sets the origin expanding to width and height
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
# Sets the width of canvas to WIDTH--does that for height as well. Make the background blue
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")

# Creates a function that can be used as a base for other uses of text function
def write_text(message, x, y):
    text = turtle.Turtle()
    text.color('black')
    text.penup()
    text.setpos(x,y)
    text.hideturtle()
    text.write(message, False, "center", ("Arial", 22, "bold"))

# Introduction message using the function defined above
write_text("Hello, welcome to this great game of rock, paper, scissors!", 0, 150)


# Canvas object
cv = screen.getcanvas()
# Hack to make window not resizable for more reliable coordinates -- resizing the window would change the coordinates of each item.
cv._rootwindow.resizable(False, False)

# Setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# Instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# Add the rock image as a shape
screen.addshape(rock_image)
# Attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# Remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
# Assign variables for rock position
rock_pos_x = -300
rock_pos_y = 0
# Set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)

# Sets a new image to the cpu
rock_image_cpu = os.path.join(images_folder, 'rock_cpu.gif')
rock_instance_cpu = turtle.Turtle()

# A function setting a position to user_rock
def user_rock(x,y):
    screen.addshape(rock_image)
    rock_instance.shape(rock_image)
    rock_instance.penup()
    rock_instance.setpos(x,y)

# A function setting a position to cpu_rock
def cpu_rock(x,y):
    screen.addshape(rock_image_cpu)
    rock_instance_cpu.shape(rock_image_cpu)
    rock_instance_cpu.penup()
    rock_instance_cpu.setpos(x,y)

# Same set of lines as above, but with paper
paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
screen.addshape(paper_image)
paper_instance.shape(paper_image)
paper_instance.penup()
paper_pos_x = 0
paper_pos_y = 0
paper_instance.setpos(paper_pos_x,paper_pos_y)

paper_image_cpu = os.path.join(images_folder, 'paper_cpu.gif')
paper_instance_cpu = turtle.Turtle()

def user_paper(x,y):
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_instance.setpos(x,y)

def cpu_paper(x,y):
    screen.addshape(paper_image_cpu)
    paper_instance_cpu.shape(paper_image_cpu)
    paper_instance_cpu.penup()
    paper_instance_cpu.setpos(x,y)

# Same set of lines as above, but with scissors
scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
screen.addshape(scissors_image)
scissors_instance.shape(scissors_image)
scissors_instance.penup()
scissors_pos_x = 300
scissors_pos_y = 0
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

scissors_image_cpu = os.path.join(images_folder, 'scissors_cpu.gif')
scissors_instance_cpu = turtle.Turtle()

def user_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

def cpu_scissors(x,y):
    screen.addshape(scissors_image_cpu)
    scissors_instance_cpu.shape(scissors_image_cpu)
    scissors_instance_cpu.penup()
    scissors_instance_cpu.setpos(x,y)

# Makes computer choose between rock, paper, or scissors
def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

# This function uses an x, y value, and obj
# In other words, creates a region for collison with cursor to indicate selection of rock, paper, or scissors
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# Sets various possibilities: If I chose __, and computer chose __, then __.
def mouse_pos(x,y):
    print("The computer chose", cpu_select())
    cpu_picked = cpu_select()
    if collide(x, y, rock_instance, rock_w, rock_h):
        print("I collided with rock")
        if cpu_picked == "rock":
            # Added for clarity. Just to see if the terminal aligns with the image.
            print("You: rock  CPU: rock")
            # Makes the text go to the left (Your choice)
            write_text("Your choice:", -300, -175)
            # Makes the text go to the right (Computer's choice)
            write_text("Computer's choice:", 300, -175)
            # Makes the scissors go off screen
            user_scissors(1200, 0)
            # Makes the paper go off screen
            user_paper(-1200, 0)
            # Sets the cpu selection of rock to the right side
            cpu_rock(300, 0)
            # Sets the user selection of rock to the left side
            user_rock(-300, 0)
            # Prints a possibility: "a tie"
            write_text("Wow, it's a tie!", 0, 0)
            # A message to indicate that you cannot continue playing on this screen--you must close out to play again
            write_text("Please reset the screen to play again.", 0, 121)
        if cpu_picked == "paper":
            print("You: rock  CPU: paper")
            write_text("Your choice:", -300, -175)
            write_text("Computer's choice:", 300, -175)            
            user_scissors(1200, 0)
            user_paper(-1200, 0)            
            user_rock(-300, 0)
            cpu_paper(300, 0)
            write_text("Haha... you lost!", 0, 0)
            write_text("Please reset the screen to play again.", 0, 121)
        if cpu_picked == "scissors":
            print("You: rock  CPU: scissors")
            write_text("Your choice:", -300, -175)
            write_text("Computer's choice:", 300, -175)            
            user_paper(1200, 0)
            user_scissors(-1200, 0)  
            user_rock(-300, 0)
            cpu_scissors(300, 0) 
            write_text("I can't believe it. You won!", 0, 0) 
            write_text("Please reset the screen to play again.", 0, 121)
    elif collide(x, y, paper_instance, paper_w, paper_h):
        print("I collided with paper")
        if cpu_picked == "rock":
            print("You: paper  CPU: rock")
            write_text("Your choice:", -300, -175)
            write_text("Computer's choice:", 300, -175)            
            user_scissors(1200, 0)
            user_rock(-1200, 0)            
            user_paper(-300, 0)
            cpu_rock(300, 0) 
            write_text("I can't believe it. You won!", 0, 0)  
            write_text("Please reset the screen to play again.", 0, 121) 
        if cpu_picked == "paper":
            print("You: paper  CPU: paper")
            write_text("Your choice:", -300, -175)
            write_text("Computer's choice:", 300, -175)            
            user_scissors(1200, 0)
            user_rock(1200, 0)
            cpu_paper(300, 0)
            user_paper(-300, 0)  
            write_text("Wow, it's a tie!", 0, 0)   
            write_text("Please reset the screen to play again.", 0, 121)   
        if cpu_picked == "scissors":
            print("You: paper  CPU: scissors")
            write_text("Your choice:", -300, -175)
            write_text("Computer's choice:", 300, -175)            
            user_scissors(1200, 0)
            user_rock(-1200, 0)
            cpu_scissors(300, 0)
            user_paper(-300, 0)   
            write_text("Haha... you lost!", 0, 0)  
            write_text("Please reset the screen to play again.", 0, 121)          
    elif collide(x, y, scissors_instance, scissors_w, scissors_h):
        print("I collided with scissors")
        if cpu_picked == "rock":
            print("You: scissors  CPU: rock")
            write_text("Your choice:", -300, -175)
            write_text("Computer's choice:", 300, -175)            
            user_rock(1200, 0)             
            user_paper(-1200, 0)
            cpu_rock(300, 0)
            user_scissors(-300, 0)              
            write_text("Haha... you lost!", 0, 0)
            write_text("Please reset the screen to play again.", 0, 121) 
        if cpu_picked == "paper":
            print("You: scissors  CPU: paper")
            write_text("Your choice:", -300, -175)
            write_text("Computer's choice:", 300, -175)            
            user_paper(1200, 0)             
            user_rock(-1200, 0)
            cpu_paper(300, 0)
            user_scissors(-300, 0)
            write_text("I can't believe it. You won!", 0, 0)
            write_text("Please reset the screen to play again.", 0, 121)  
        if cpu_picked == "scissors":
            print("You: scissors  CPU: scissors")
            write_text("Your choice:", -300, -175)
            write_text("Computer's choice:", 300, -175)            
            user_paper(-1200, 0)
            user_rock(1200, 0)
            cpu_scissors(300, 0)
            user_scissors(-300, 0)
            write_text("Wow, it's a tie!", 0, 0)
            write_text("Please reset the screen to play again.", 0, 121)               
    # elif collide(x, y, scissors_instance, scissors_w, scissors_h):
    #     print("I collided with scissors")
    # elif collide(x, y, paper_instance, paper_w, paper_h):
    #     print("I collided with paper")
    # If the user does not click one of them, it prints this message
    else: 
        write_text("Cheater! Please choose an option.", 0, -175)
        print("You didn't choose an option.")



screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()