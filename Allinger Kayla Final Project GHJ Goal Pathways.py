"""
Program: GUI Good Habit Jitsu Goal Pathways
Author: Kayla Allinger
Last date Modified: 

This is a tool to assist those interested in self development and achieving goals
to plan pathways to achieving goals with the help of visualization of those paths
and the practices and habits needed to get there."""

#import everything from tkinter
import tkinter as tk

#create a class to be the box/GUI of the intro page for this tool
#here is where attributes of widgets are applied, self is used to access the attributes
#of the class we've created, place all the widgets at the proper coordinants:
class ghjIntroWindow:
   def __init__(self, win):
       self.labl1=tk.Label(win, text='Thank you for your interest in Good Habit Jitsu tools.')
       self.labl1.place(x=600, y=50)
       
       self.labl2_text = """This path builder tool will provide visual examples of what it is to create a pathway to goals by breaking large objectives into smaller manageable tasks, and how these tasks compound to become realized goals.
       It will provide a visual aid to help you understand why creating a path to move you towards goals is so important and impactful to shaping the life you want through conscious choices and habits."""
       self.labl2= tk.Label(win, text=self.labl2_text, fg = 'blue', justify='center')
       self.labl2.place(x=200,y=100)   
       
       self.b2= tk.Button(win, text='Convert Celsius To Fahrenheit')
       self.b2.bind('<Button-1>', self.cToF)
       self.b2.place(x=660, y=175)
       
#methods created for temperature conversion formulas, and
#display them in the temp 2 entry fields
   def cToF(self, event):
       self.temp2.delete(0, 'end')
       num1=float(self.temp1.get())
       result=round(9/5* num1 +32, 2)
       self.temp2.insert(tk.END, str(result))
       
#create main application window and create instance of the tempWindow class
#set the size of the window and run the event loop
window=tk.Tk()
mywin=ghjIntroWindow(window)
window.title('Good Habit Jitsu Goal Pathways')
window.geometry("1500x800")
window.mainloop()
