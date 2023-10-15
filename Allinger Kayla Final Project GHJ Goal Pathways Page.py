"""
Program: GUI Good Habit Jitsu Goal Pathways
Author: Kayla Allinger
Last date Modified: 

This tool assumes the user as visited the "Good Habit Jitsu Website and is using a visual aid tool offered on the website

This is a tool to assist those interested in self development to plan pathways to
achieving goals with the help of visualization of those paths. It highlights the importance 
of planning and practicing and habits needed to get there."""

#import the Tkinter library to create a GUI and approprate modules
#and classes to run in the pages of the program
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from turtle import RawTurtle, Canvas
import random

#create default window
root = tk.Tk()

#load my images
image = PhotoImage(file="rockclimb1.png")
image2 = PhotoImage(file="jitshobby.png")

#create ToolTip class to add alternate text to the images.
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

#Method to be called when the mouse pointer enters the widget/image
#include the coordinates where the "tooltip" will be displayed
    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", borderwidth=1)
        label.pack()
#The method called when the pointer leaves the image
    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()

#create a class to be the box/GUI of the intro page for this tool
#here is where attributes of widgets are applied, self is used to access the attributes
#of the class we've created, place all the widgets at the proper coordinants:
class ghjIntroWindow:
   def __init__(self, win, image):
       self.win = win
       self.image = image
       self.labl1=tk.Label(win, text='Thank you for your interest in Good Habit Jitsu tools.', fg='blue', font=("Times New Roman", 20))                  
       self.labl1.pack(pady=50)
       
       self.labl2_text = """This path builder tool will provide visual examples of what it is to create a pathway to goals by breaking large objectives into smaller manageable tasks, and how these tasks compound to become realized goals.
  
       It will provide a visual aid to help you understand why creating a path to move you towards goals is so important and impactful to shaping the life you want through conscious choices and habits."""
       
       self.labl2= tk.Label(
          win,
          text=self.labl2_text,
          font=("Times New Roman", 14),
          wraplength=850)
       self.labl2.pack()   
       
       self.b2= tk.Button(win, text='Continue', command=self.show_second_page, bg='cyan', font=("Times New Roman", 10))
       self.b2.pack(pady=50)

       self.image_label1 = tk.Label(win, image=image)
       self.image_label1.pack(side=tk.LEFT)
       # Add a tooltip for the first image label
       tooltip1 = ToolTip(self.image_label1, "Rock climbing.")
       
       self.image_label2 = tk.Label(win, image=image2)
       self.image_label2.pack(side=tk.RIGHT)   
       # Add a tooltip for the second image label
       tooltip2 = ToolTip(self.image_label2, "Jiujitsu Tournament")
       
#method to make button work
   def show_second_page(self):
        self.win.withdraw()  # Hide the current window
        second_window = tk.Tk()
        mywin = SecondPage(second_window, self)
        second_window.title('Destinations with no maps.')
        second_window.geometry("1000x800+0+0")
        second_window.mainloop()


#create a class for the second page to place text and widgets
class SecondPage:
    def __init__(self, win, main_win):
        self.back_button = tk.Button(win, text='Go Back to First Page', command=self.show_first_page, bg='cyan', font=("Times New Roman", 10))
        self.back_button.pack()
        self.win = win
        self.main_win = main_win
        self.label_text ='Destinations with no maps.'
        self.label = tk.Label(
           win,
            text=self.label_text,
            font=("Times New Roman", 14),
            wraplength=850)
        self.label.pack(pady=25)

        self.label2_text = """If you are going to take a trip, do you typically leave the house without knowing where you're going,
        or how to get there?

        That sounds somewhat scary or nerve wracking doesn't it?"""
        self.label2 = tk.Label(
            win,
            text=self.label2_text,
            font=("Times New Roman", 14),
            wraplength=1000)
        self.label2.pack()

        self.label3_text = """No, when you are taking a trip you plan a destination, a method of travel, budget finances,
        pack supplies, schedule activites or possibly have an agenda for each day.
        
        It's the same with goals. A goal is a type of destination. It requires similar planning to get where you want to go."""
        self.label3 = tk.Label(
            win,
            text=self.label3_text,
            font=("Times New Roman", 14),
            wraplength=1000)
        self.label3.pack()

        self.label4_text = """For a visual aid of this concept, click below to see how difficult it will be to reach a destination with no plans or map."""
        self.label4 = tk.Label(
            win,
            text=self.label4_text,
            font=("Times New Roman", 14),
            wraplength=1000)
        self.label4.pack()

        self.start_button = tk.Button(win, text='Start with no plans!', command=self.start_turtle_walk,bg='cyan', font=("Times New Roman", 10))
        self.start_button.pack()
#the turtle wald begins at "False" as the walk does not begin until the user
#clicks start
        self.turtle_walk_started = False
      
        #create a canvas for the turtle 
        self.canvas = Canvas(win, width=400, height=400)
        self.canvas.pack()

        # Create a turtle and configure it on the canvas
        self.t = RawTurtle(self.canvas)
        self.t.hideturtle()
        self.t.speed(3)
        self.t.penup()
        #position "Goal" in upper right
        self.t.goto(160, 160)
        self.t.write("Goal", align="right", font=("Times New Roman", 14, "normal"))
        self.t.goto(-180, -180)  # Set initial position close to the bottom-left corner
        self.t.pendown()
        self.t.showturtle()
             
        self.next_button = tk.Button(win, text='Continue', command=self.show_third_page,bg='cyan', font=("Times New Roman", 10))
        self.next_button.pack()

#define a method to start the turtle walk, it uses an if statement to
#determine the check if the "turtle_walk_started" attribute is true or false
    def start_turtle_walk(self):
        if not self.turtle_walk_started:
            self.turtle_walk_started = True
            self.randomWalk(self.t, 100)

    # Method/function for a random turtle walk
    def randomWalk(self, t, turns, distance=75):
        for x in range(turns):
            if x % 2 == 0:
                t.left(random.randint(0, 180))
            else:
                t.right(random.randint(0, 270))
            t.forward(distance)   
       

#method functions to control navigation with the buttons:
    def show_first_page(self):
        self.win.withdraw()  # Close the current window
        self.main_win.win.deiconify()  # Show the main window

    def show_third_page(self):
        self.win.withdraw()  # Close the current window
        third_window = tk.Tk()
        mywin = ThirdPage(third_window, self.main_win)
        third_window.title('Planned Pathways')
        third_window.geometry("1000x800+0+0")
        third_window.mainloop()


#create a class for the 3rd page
class ThirdPage:
    def __init__(self, win, main_win):
        
        self.win = win
        self.main_win = main_win        
        self.label_text = 'Planning smaller steps and good habits.'
        self.label = tk.Label(
           win,
           text=self.label_text,
           font=("Times New Roman", 14),
           wraplength=850)
        self.label.pack()

        self.label2_text = """Whether you want to learn to code, get in shape or learn to play a musical instrument,
        now lets see the impact planning will have on reaching a big goal.\n
        Choose an example goal below, and the habits that you think will help reach that goal in a given time frame.\n"""
        self.label2 = tk.Label(
            win,
            text=self.label2_text,
            font=("Times New Roman", 14),
            wraplength=1000)
        self.label2.pack()

     #Code for dropdowns and their labels:   

        self.label3_text = """Select Goal:"""
        self.label3 = tk.Label(
            win,
            text=self.label3_text,
            font=("Times New Roman", 12),
            wraplength=1000)
        self.label3.pack()

        
        # Create a list of options for the first dropdown (Goal)
        options_goal1 = ["Learn to Code", "Get in Shape", "Learn a Musical Instrument"]
        # Create a variable to store the selected option for Goal
        selected_option_goal1 = tk.StringVar()
        selected_option_goal1.set(options_goal1[0])  # Set the default selected option
        
        self.goal_dropdown1 = tk.OptionMenu(win, selected_option_goal1, *options_goal1)
        self.goal_dropdown1.pack()

#use similar code to create the rest of the dropdowns and labels:
        self.label4_text = """       Habit in Month 1:"""
        self.label4 = tk.Label(
            win,
            text=self.label4_text,
            font=("Times New Roman", 12),
            wraplength=1000)
        self.label4.pack()

        #Habits 1
        #First Habit dropdown
        # Create a list of options for the first habit dropdown (Habits to obtain Goal)
        options_habits_goal1 = ["Watch an introductory coding video on YouTube", "Just think about it without taking action","Decide if you want to gain muscle or boost cardio", "Wonder what life would be like with a change, but take no action","Decide what instrument to play"]
        # Create a variable to store the selected options 
        selected_option_habits_goal1 = tk.StringVar()
        selected_option_habits_goal1.set(options_habits_goal1[0])  # Set the default selected option

        # Create the first habit dropdown selection box for Habits of Goal 1
        self.habits_dropdown1 = tk.OptionMenu(win, selected_option_habits_goal1, *options_habits_goal1)
        self.habits_dropdown1.pack()

        self.label5_text = """      Habit in Month 2:"""
        self.label5 = tk.Label(
            win,
            text=self.label5_text,
            font=("Times New Roman", 12),
            wraplength=1000)
        self.label5.pack()

        #habits 2
        # Create a list of options for the second habit dropdown (Habits for Goal chosen)
        options_habits_goal1_2 = ["Pick a specific coding language", "Read Reddit threads about the thing you like doing, but take no action","Pick a specific exercise program geared towards your goal", "Participate in music lessons","Tell people you would like to learn code, get in shape or learn a musical instrument, but lay on the couch all day after work", "Stick to a sleep schedule", "Eat fruits and vegetables"]
        # Create a variable to store the selected options
        selected_option_habits_goal1_2 = tk.StringVar()
        selected_option_habits_goal1_2.set(options_habits_goal1_2[0])  # Set the default selected option

        # Create the second habit dropdown selection box for Habits
        self.habits_dropdown1_2 = tk.OptionMenu(win, selected_option_habits_goal1_2, *options_habits_goal1_2)
        self.habits_dropdown1_2.pack()

        self.label6_text = """      Habit in Month 3:"""
        self.label6 = tk.Label(
            win,
            text=self.label6_text,
            font=("Times New Roman", 12),
            wraplength=1000)
        self.label6.pack()

        #habits 3
        # Continue to create lists of options for the 3rd dropdown (Habits for the Goal Chosen)
        options_habits_goal2 = ["Follow an online tutorial to learn the basics of your coding language", "Show up for your workout every day, even if you don't plan to complete it, just show up.", "Decide you will do it tomorrow", "Practice a specific piece of music for 30 minutes per day", "Wish you knew how to code, play an instrument or were in shape, but get overwhelmed by how to get started and take no action", "Join an online community focused on the skill you are working to learn and actively participate", "Exercise at least 30 minutes each day"]
        # Create a variable to store the selected option for Habits
        selected_option_habits_goal2 = tk.StringVar()
        selected_option_habits_goal2.set(options_habits_goal2[0])  # Set the default selected option

        # Create the third habit dropdown selection box for Habits of Goal 2
        self.habits_dropdown2 = tk.OptionMenu(win, selected_option_habits_goal2, *options_habits_goal2)
        self.habits_dropdown2.pack()
        self.label7_text = """       Habit in Month 4:"""
        self.label7 = tk.Label(
            win,
            text=self.label7_text,
            font=("Times New Roman", 12),
            wraplength=1000)
        self.label7.pack()

        #habits 4
        # Create a list of options for the 4th habit dropdown
        options_habits_goal3 = ["Complete an intermediate level coding project", "Complete an entire crossfit boot camp", "Learn a complete song or two on your musical instrument", "Add a project to your coding portfolio", "Run a 5k"]
        # Create a variable to store the selected option for Habits 
        selected_option_habits_goal3 = tk.StringVar()
        selected_option_habits_goal3.set(options_habits_goal3[0])  # Set the default selected option

        self.habits_dropdown3 = tk.OptionMenu(win, selected_option_habits_goal3, *options_habits_goal3)
        self.habits_dropdown3.pack()

        self.start_turtle_button = tk.Button(win, text='Start with Plans!', command=self.start_turtle_walk, bg='cyan', font=("Times New Roman", 10))
        self.start_turtle_button.pack()

        self.turtle_walk_started = False

        # Create a canvas for the turtle
        self.turtle_canvas = Canvas(win, width=200, height=200)
        self.turtle_canvas.pack()

        self.label8_text = """Now you have a better understanding of how planning a course and good habits will help you to reach your goals!
        Thank you!"""
        self.label8 = tk.Label(
            win,
            text=self.label8_text,
            font=("Times New Roman", 12),
            wraplength=1000)
        self.label8.pack()
#code for exit button:
        self.exit_button = tk.Button(win, text='Exit', command=self.exit_program, bg='cyan', font=("Times New Roman", 10))
        self.exit_button.pack() 

        # Create a turtle and configure it on the canvas
        self.turtle = RawTurtle(self.turtle_canvas)
        self.turtle.hideturtle()
        self.turtle.speed(3)
        self.turtle.penup()
        #position "Goal" in upper right
        self.turtle.goto(75, 75)
        self.turtle.write("Goal", align="right", font=("Times New Roman", 14, "normal"))
        self.turtle.goto(-75, -75)  # Set the initial position close to the bottom-left corner
        self.turtle.pendown()
        self.turtle.showturtle()

    def start_turtle_walk(self):
        if not self.turtle_walk_started:
            self.turtle_walk_started = True
            self.random_walk(self.turtle, 100)

#similar coding for new turtle walk, but with set directions to move up in steps
    def random_walk(self, t, turns, distance=20):
        for x in range(turns):
            if x % 4 == 0:
                # Move upward
                t.setheading(90)  # Set the direction to up (90 degrees)
            elif x % 4 == 1:
                # Move to the right
                t.setheading(0)  # Set the direction to right (0 degrees)
            elif x % 4 == 2:
                # Move upward
                t.setheading(90)  # Set the direction to up (90 degrees)
            else:
                # Move to the right
                t.setheading(0)  # Set the direction to right (0 degrees)
            t.forward(distance)          

#method funtcions for button navigation
    def show_second_page(self):
        self.win.withdraw()  # Close the current window
        second_window = tk.Tk()
        mywin = SecondPage(second_window, self.main_win)
        second_window.title('Destinations with no maps.')
        second_window.geometry("1000x800+0+0")
        second_window.mainloop()

    def exit_program(self):
        self.win.withdraw()  # Close the current window to exit the program

                      
#create main application window and create instance of the ghjIntroWindow class
#set the size of the window/geometry for screen placement and run the event loop
mywin=ghjIntroWindow(root, image)
root.title('Good Habit Jitsu Goal Pathways')
root.geometry("1000x800+0+0")
root.mainloop()
