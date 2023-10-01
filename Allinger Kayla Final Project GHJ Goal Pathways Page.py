"""
Program: GUI Good Habit Jitsu Goal Pathways
Author: Kayla Allinger
Last date Modified: 

This tool assumes the user as visited the "Good Habit Jitsu Website and is 

This is a tool to assist those interested in self development to plan pathways to
achieving goals with the help of visualization of those paths. It highlights the importance 
of planning and practicing and habits needed to get there."""

#import everything from tkinter
import tkinter as tk

#create a class to be the box/GUI of the intro page for this tool
#here is where attributes of widgets are applied, self is used to access the attributes
#of the class we've created, place all the widgets at the proper coordinants:
class ghjIntroWindow:
   def __init__(self, win):
       self.win = win
       self.labl1=tk.Label(win, text='Thank you for your interest in Good Habit Jitsu tools.')
       self.labl1.pack(pady=50)
       
       self.labl2_text = """This path builder tool will provide visual examples of what it is to create a pathway to goals by breaking large objectives into smaller manageable tasks, and how these tasks compound to become realized goals.
       It will provide a visual aid to help you understand why creating a path to move you towards goals is so important and impactful to shaping the life you want through conscious choices and habits."""
       self.labl2= tk.Label(win, text=self.labl2_text, fg = 'blue', justify='center')
       self.labl2.pack(pady=50)   
       
       self.b2= tk.Button(win, text='Continue', command=self.show_second_page)
       self.b2.pack(pady=50)
       
#function to make button work
   def show_second_page(self):
        self.win.withdraw()  # Hide the current window
        second_window = tk.Tk()
        mywin = SecondPage(second_window, self)
        second_window.title('Destinations with no maps.')
        second_window.geometry("1500x800")
        second_window.mainloop()

#create a class for the second page
class SecondPage:
    def __init__(self, win, main_win):
        self.win = win
        self.main_win = main_win
        self.label = tk.Label(win, text='This is the Second Page')
        self.label.pack(pady=50)

        self.next_button = tk.Button(win, text='Go to Third Page', command=self.show_third_page)
        self.next_button.pack()

        self.back_button = tk.Button(win, text='Go Back to First Page', command=self.show_first_page)
        self.back_button.pack()

#functions to make buttons work
    def show_first_page(self):
        self.win.withdraw()  # Close the current window
        self.main_win.win.deiconify()  # Show the main window

    def show_third_page(self):
        self.win.destroy()  # Destroy/Close the current window
        third_window = tk.Tk()
        mywin = ThirdPage(third_window, self.main_win)
        third_window.title('Planned Pathways')
        third_window.geometry("1500x800")
        third_window.mainloop()


#create a class for the 3rd page
class ThirdPage:
    def __init__(self, win, main_win):
        self.win = win
        self.main_win = main_win
        self.label = tk.Label(win, text='This is the Third Page')
        self.label.pack(pady=50)     

        self.back_button = tk.Button(win, text='Go Back to Second Page', command=self.show_second_page)
        self.back_button.pack()

        self.exit_button = tk.Button(win, text='Exit', command=self.exit_program)
        self.exit_button.pack()

#funtcions to make buttons work
    def show_second_page(self):
        self.win.destroy()  # Close the current window
        second_window = tk.Tk()
        mywin = SecondPage(second_window, self.main_win)
        second_window.title('Destinations with no maps.')
        second_window.geometry("1500x800")
        second_window.mainloop()

    def exit_program(self):
        self.win.destroy()  # Close the current window to exit the program
        

        
       
#create main application window and create instance of the tempWindow class
#set the size of the window and run the event loop
window=tk.Tk()
mywin=ghjIntroWindow(window)
window.title('Good Habit Jitsu Goal Pathways')
window.geometry("1500x800")
window.mainloop()
