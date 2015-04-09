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
"You get off work and you get called by your roommate on the way home and asks you to go to the store and pick up some vegetables for dinner." + \
                    "you say you can, so you go to the local grocery store and buy some vegetables." + \
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
        gchp2()
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
def choice9():
    choice = simpledialog.askinteger("You arrive at Farquaads palace and meet him. He proposes a deal with you." + \
                                     "The deal proposes for you to be immortal and hunt down all who praise shrek for him" + \
                                     "Do you take the deal or not?")
    if (choice == 1):
        messagebox.showinfo("Take the deal",
                            "You join his side, he hands you a potion labeled Immortality. you drink it and it and he reveals to you that you will slowly die." + \
                            "He forces you to work for himi now as you slowly die. If you kill all who follow shrek he will give you the cure. THE END")
    elif (choice == 2):
        messagebox.showinfo("Refuse",
                            "You refuse the deal and anger him. He chrages you drawing his sword, as he get within swinging distance you hear a roar. unsure what it is you punch him in the face and take his sword." + \
                            "Before you get a chance to swing a dragon bursts throught the wall infront of you and eats him. The dragon then flies away. THE END.")
    else:
        choice9()

    
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
        choice4()
    else:
        choice3()
def choice4():
    choice = simpledialog.askinteger( "My Little Pony: Friendship Undone..." , " You get to your house and when you get to your door you hear a soft" +\
                                      "'laddeh' flow through the air" +\
                                      " along with a scent of onions wafting. When you open your door you see an onion. Do you pick it up?")
    if (choice == 1):
        messagebox.showinfo("The Crying Game..." , "You pick up the onion and immediately fall to the floor in tears. You dont know why, but you feel like you" +\
                            " couldve done...more with your life. You spend 75 years crying at your door. THE END.")
    elif (choice == 2):
        messagebox.showinfo("House fire..." , "You kick the onion aside and go for the gasoline in your garage. After pouring gasoline on everything, you" +\
                            "burn everything in the house, including you. THE END.")
    else:
        choice4()
    
    

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
##################Gordon Chapter 2#############################
def gchp2():
    choice = simpledialog.askinteger("It's been 500 years since the glorious Great Swamp Beyond came back down to the physical realm. Everyone" +\
                                     "is happy , world population in skyrocketing, hunger and disease is non existant. Unfortunately, no one has" +\
                                     "seen or heard from Shrek himself or the holy follower that brought him back in a month. The masses are beggining" +\
                                     "to panic, and on the way home from the local onion flavored ice cream shoppe, a robed man approaches you. he says" +\
                                     " ' Bonquiqui, asw you may have heard, shrek has gone missing. The truth of that is Prince Charming has incited" +\
                                     " another rebellion against Shrek and taken him captive. Right now, Shreks forces are fighting Charming and we" +\
                                     "cant get anyone to go get Shrek, so you are our only hope, since Charming wont expect a civilian to come save" +\
                                     "our lord and savior, the green one himself.' do you take him up on his offer and go save Shrek?")
    if (choice == 1):
        messagebox.showinfo("Lets get down to business to defeat, the prince..." , "You take up the hooded figure on his offer to free shrek")
        choiceq1yes()
    elif (choice ==2):
        messagebox.showinfo("DECAPATATIOOOOOOOOOOOOOOOON" , "The hooded man decapatates you right on the spot for not being devoted to Shrek. THE END")
    else:
        choicegchp2()
################ JP's Work ########################
def cpt2():
    choice = simpledialog.askinterger("New Begingings","5 years after the death of Lord Farquaad, you still work for the same company but now you are the CEO." \
                                      "You get a strange leter on your desk, it tell you to meet up with an old friend at Farquaad's castle." \
                                      "Do you go? 1 to go 2 not to go")
    if (choice == 1):
        rick()
    elif (choice == 2):
        norisk()
    else:
        cpt2()
def risk():
    choice = simpledialog.askinterger("risk", "You call your assistant taking some time off. You go home, not knowing what to expect and arm your self. you grab a knife, a pistol and a rifle." \
                             "you drive to the castle and walk in. As you walk in you see that it has been abandoned. You walk up to the throne room as the letter told you to." \
                             "Sitting in the the throne is a big dark fiqure. Its shrek! Alerted you draw you knife. Do you slice or stab? 1 for slice 2 for stab.")
    if (choice == 1):
        cut()
    elif (choice == 2):
        stab()
    else:
        risk()
def norisk():
    choice = simpledialog.askinterger(
################ Winikka's Work #####################
# TODO: Add my functions below

################ Main #####################
intro()

root.destroy()
