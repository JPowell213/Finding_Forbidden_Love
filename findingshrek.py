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
    messagebox.showinfo("Title", "\n You are a normal person with a job at a worldwide company. Work has been a bit stressful lately." + \
                        "You get off work and you get called by your roommate calls you on the way home and asks you to go to the store and pick up some vegitables for dinner." + \
                        "you say you can, so you go to the local grocery store and buy some vegitable." + \
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
    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You didn't pick up the onion. You go on a drive to think about something that n\
has been happening at your job, and suddenly you hear a roar on an engine as you see the batmobile come out of no where and fly n\
right next to you then you see an explosive batarang hit your car and blow up your car...THE END")
    else:
        choice1()
def choice6():
    choice = simpledialog.askinteger("The OgreLord",
                                     "You have summoned Shrek in to the world, now you have a choice. Betray Shrek or side with him")

    if (choice == 1):
        messagebox.showinfo("The betrael",
                            "Shrek lets out a ogre roar, you are frightened and you enter a fighting stance")
        choice7()
    elif (choice == 2):
        messagebox.showinfo("The Great Swamp",
                            "The Great swamp beyond resides down to earth and takes you with it, THE END")
    else:
        choice6()

def choice7():
    choice = simpledialog.askinteger("The fight",
                                     "As you enter your fighting stance you find a weak point in shreks defences," + \
                                     "Do you kick or punch Shrek?" + \
                                     "1. Kick" + \
                                     "2. Punch")
    if (choice == 1):
        messagebox.showinfo("Kick",
                            "You go for the kick but shrek catches your foot and throws you around the earth, as you come back around he punches you in the face ending the fight and your life, THE END.")
    elif (choice == 2):
        messagebox.showinfo("Punch",
                            "Useing you past experience with MMA and sumo wrestling you punch Shrek causing him to fall into a vat of flowers and melt.")
        choice8()
    else:
        choice7()
def choice8():
    choice = simpledialog.askinteger("Defeat....",
                                   "You defeated shrek and a knight walks up to you. you have no idea where this knight came from but he wants to deliver a message to you." + \
                                   "The message says, 'Dear valiant citizen, I am Lord Farquaad and I am summoning you to my palace to talk about a deal between you and me." + \
                                   "Do you go? 1. Go 2.Don't Go")
    if (choice == 1):
        messagebox.showinfo("Yes",
                            "You decide to go, and a horse appears from thin air and you ride to the palace with the knight.")
        choice9()
    elif (choice == 2):
        messagebox.showinfo("No",
                            "You have decided not to go to the palace and you start to walk away from the knight you hear a draggon roar and a dragon ridden by a donkey swoops down" + \
                            " and eats you then spits you out then flys away. THE END")
    else:
        choice8()

    
    
################ Gordon's Work #####################
def choice1():
    choice = simpledialog.askinteger("you buy the onion",
                                     "You leave the gorcery store and see a sign on the street for a local library. the sign says 'free books!' go get book?")
    if (choice == 1):
        messagebox.showinfo(" freeee book " , "you chose to go to the library and get a freeeeeeeee book.",)
        choice3() 

    elif (choice == 2):
        messagebox.showinfo("ouch...",
                            "you decide not to go to the library. As you walk down the sidewalk, you lip and fall on a onion peel, n\
     headfirst into the ground and along ewith that headfirst into a coma untill you die. \
     you live the rest of your natural life as a vegitable. THE END.")
    else:
        choice1()
def choice3():
    choice = simpledialog.askinteger("The Library" , "You arrive at the library and you see only 2 books left to choose for the free books, \
a book titled 'Forbidden Onion Magic' and another called 'My Little Pony: Flutterbutts Power' which do you choose?")
    if (choice == 1):
        messagebox.showinfo("The Power Of The Onion..." , "As soon as you pick up the book the clouds outside. You rush outside as a large meteor soars down through the parted clouds.")
        choice5()
    elif (choice == 2):
        messagebox.showinfo("Flutterbutts Demise...." , "you pick up the MLP book and head back to your car to head home.")
    else:
        choice3()
    

def choice5():
    choice = simpledialog.askinteger( "The meteor..." , "The meteor crash lands right infront of you. From the meteor, " + \
                                           "an onion starts hovering into the air and slowly starts coming towards you." + \
                                           "As soon as the onion starts floating towards you, the onion magic book flies " + \
                                           "from your hand and starts flipping pages untill it gets to the page titled 'Summoning Shrek'. " + \
                                           "Do you summon Shrek?")

    if (choice == 1):
        messagebox.showinfo("The Shrekoning..." , "You decide to summon the Ogrelord back into the physical realm")
        choice6()
    elif (choice == 2):
        messagebox.showinfo("The Onion Sadness..." , "You decide not to summon Shrek")
    else:
        choice5()
                                    
################ Main #####################
intro()
root.destroy()
