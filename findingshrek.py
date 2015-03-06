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
    messagebox.showinfo("Title", "\nHello, you are a _____ from ____. " + \
                        "You stumble across such and such.")
    choice = simpledialog.askinteger("Choose wisely",
                                   "You have a choice to pick: 1 or 2.")
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        intro()

################ JP's Work #####################
def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "You didn't buy an onion and you go into the garage to put some groceries away and you find an onion.  Do you pick it up? 1 or 2.")
    if (choice == 1):
        messagebox.showinfo("Yes",
                            "You pick up the onion and go for a drive to think, as your driving you see the batmobile fly right next to you and n\
you see a batarange get knocked out of the air as if it hit something and you live on as if nothing happened.  THE END")
    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You didn't pick up the onion. You go on a drive to think about something that n\
has been happening at your job, and suddenly you hear a roar on an engine as you see the batmobile come out of no where and fly n\
right next to you then you see an explosive batarang hit your car and blow up your car...THE END")
    else:
        choice1()

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
