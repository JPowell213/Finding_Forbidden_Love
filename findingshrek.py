# Choose.py
# by Johnathan Powell & Gordon Jiroux
# Description: starter code for the Choose Your
# Own Adventure Project

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "\n You are a normal person with a job at a worldwide company. Work has been a bit stressful lately. \
 You get off work and you get called by your roommate you on the way home and asks you to go to the store and pick up some vegitables for dinner. n\
you say you can, so you go to the local grocery store and buy some vegitable." + \
                        "You stumble across the onions section and you look at the onions.")
    choice = simpledialog.askinteger("Do you buy an onion?",
                                   "you must choose 1 or 2. 1 for Buying the onion,2 for not buying the onion.")
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        intro()

################ JP's Work #####################
def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "You didn't buy an onion and you go home and then into the garage to put some groceries away and you find an onion.  Do you pick it up? 1 or 2.")
    if (choice == 1):
        messagebox.showinfo("Yes",
                            "You pick up the onion and go for a drive to think, as your driving you see the batmobile fly right next to you and n\
you see a batarange get knocked out of the air as if it hit something and you live on as if nothing happened.  THE END")
        choice3() 
        
    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You didn't pick up the onion. You go on a drive to think about something that n\
has been happening at your job, and suddenly you hear a roar on an engine as you see the batmobile come out of no where and fly n\
right next to you then you see an explosive batarang hit your car and blow up your car...THE END")
    else:
        choice1()
def choice3():
    messagebox.showinfo("You did it bitch", "you did it bitch")

################ Gordon's Work #####################
def choice1():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()

################ Main #####################
intro()

root.destroy()
