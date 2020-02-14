#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 17:52:46 2018

@author: chase.kusterer
"""

"""
    DocString:
    
    A) Introduction:
    This game is based on the movie Monty Python and the Holy Grail
    (1975). It consists of three stages, and also has defined functions
    for start, win, and lose. This game requires honesty, and having a
    small amount of knowledge from the movie will be helpful.
    
    Round 1: Decide whether or not to approach the bridge.
    Round 2: Cross the Bridge of Death
    Round 3: Defeat the Black Knight
    
    B) Known Bugs and/or Errors:
    None.
    
"""

from sys import exit
import random

def start():
    print("""
         As you start on your journey, you see a bridge in the
         distance. It stretches over a furious volcano. You need to
         cross it in order to continue your quest for the Holy Grail.
         """)
    input("<Press enter to continue>\n")
    starting_path()

def starting_path():
    print("""
    As the leader of the quest, what would you like to do?
    1) approach the bridge.
    2) rest here an decide later.
    3) run away!
    """)
    
    choice = input(">  \n")

    if "1" in choice or "approach" in choice or "bridge" in choice:
        print("\nYou're off to the bridge!\n")
        input("<Press enter to continue>\n")
        bridge_area()
    
    elif "2" in choice or "rest" in choice or "later" in choice:
        print("""\nNow that you're rested, what would you like to do?.""")
        input("<Press enter to continue>\n")
        starting_path()
    
    elif "3" in choice or "run" in choice:
        print("\nWell I guess the quest is over. Good-bye!")
        exit(0)
    
    else:
        print("Invalid command. Please try again.")
        input("<Press enter to continue>\n")
        starting_path()


def bridge_area():
    print("""
As you're about to start crossing the bridge, a wizard cuts
in front of you and shouts:
              
              "STOP. Who would cross the Bridge of Death must answer me
              these questions three, ere the other side he see." 
        
In this, you must truthfully answer three questions.
          """)
    
    question_list = ['What... is your name?',
                     'What... is your quest?',
                     'What... is your favorite color?',
                     'What... is the capital of Assyria?',
                     'What... is the air-speed velocity of an unladen swallow?']
    questions = 3
    
    while questions > 0:
        question = random.choice(question_list)
        input("<Press enter for your question>\n")
        print(question)
        print(" ")
        
        if question == question_list[0]:
            print("You can input anything and you're ok.")
            name = input("Your name: \n")
            print(f"WIZARD: Nice to meet you {name}!")
            questions -=1
        
        elif question == question_list[1]:
            print("1) I am on a quest for the Holy Grail")
            print("2) I am NOT on a quest for the Holy Grail.")
            print("3) I forgot.")
            
            quest = input("> \n")
            
            if quest == '1':
                print("Thanks for letting me know. It's kind of lonely guarding this bridge all the time.\n")
                questions -=1
            
            else: 
                print("You fly high into the air and land in the volcano.")
                fail()

        elif question == question_list[2]:
            print("You can choose any primary color.\n")
            color = input("> \n")
            color = color.lower()
            
            if 'red' in color or 'blue' in color or 'yellow' in color:
                print("WIZARD: I like that color too!\n")
                questions -=1
            
            else:
                print("WIZARD: What? That's not a primary color!")
                print("You fly high into the air and land in the volcano.\n")
                fail()
        
        elif question == question_list[3]:
            print("1) Keep silent until the wizard gets bored.")
            print("2) Try to guess.\n")
        
            guess = input("> \n")
        
            if '1' in guess or 'silent' in guess or 'bored' in guess:
                print("WIZARD: Ok, ok, I will give you a freebie.\n")
                questions -= 1
            
            elif '2' in guess or 'try' in guess or 'guess' in guess: 
                 input("Your guess: \n")
                 print("WIZARD: Ha! I made that place up!")
                 print("You fly high into the air and land in the volcano.")
                 fail()
            
        elif question == question_list[4]:
            print("1) 62.3 meters per second")
            print("2) 63.2 meters per second")
            print("3) What do you mean? An African or European swallow?\n")
            
            swallow = input("> \n")
            
            if '1' in swallow or '62.3' in swallow or '2' in swallow or '63.2' in swallow:
                print("You fly high into the air and land in the volcano.")
                fail()
            
            elif '3' in swallow or 'African' in swallow or 'European' in swallow:
                print("WIZARD: Huh? I... I don't know that.")
                print("WIZARD: Ahhhhhh.\n")
                print("The wizard flies into the volcano and you are free to pass.")
                
                break
            
    print("You made it across the Bridge of Death!\n")
    input("<Press enter to continue>\n")
    black_knight()

def black_knight():
    print("""
You are across the bridge and on your way to the Holy Grail when the
Black Knight pops out to challenge you.
""")
    print("What do you do?")
    print("1) Attack with your sword")
    print("2) Run away!")
    
    knight = input("> \n")
    
    if '1' in knight or 'attack' in knight or 'sword' in knight:
        print("You attack with your sword and cut the Black Knight's arm off.")
        print("The black night yells: 'Tis but a scratch' and runs away.\n")
        input("<Press enter to continue>\n")
        grail()
    
    elif '2' in knight or 'run' in knight:
        print('You end up back at the bridge.')
        bridge_area()


def grail():
    print("""
You have completed your quest for the Holy Grail! Great job!
          """)
    input("<Press enter to exit, you champion!>\n")
    exit(0)
    
def fail():
    print('\nYou have failed in your quest for the Holy Grail.')
    input('<Game Over>')
    exit(0)

start()

