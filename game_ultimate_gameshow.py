#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:09:01 2018

@author: chase.kusterer
"""

"""
DocString:
    
    A) Introduction:
    As you may have guessed, this is THE ultimate gameshow. This game
    consists of three rounds... all requiring luck and, well, just
    luck. There is no skill involved.
    
    Round 1: Coin toss
    Round 2: Guess the suit of a random card from a deck of 52 cards
    Round 3: Find a prize (or your least favorite food behind one of
             three doors

    B) Known Bugs and/or Errors:
    None.

"""

from sys import exit
from random import randint

def game_start():
    global host_name
    global contestant_name
    global country
    global hate_food
    
    print("\nHello and welcome once again to THE ULTIMATE GAMESHOW!!!\n")
    input('<Press any key to continue>\n')
    
    print("My name is... uhhh ... my name is... well, you all know my")
    print("name! It's... \n")
    host_name = input('Input host name: \n')
    
    print(f"\nYes, thank you, my name is {host_name}!")
    print("""
Today we welcome our contestant that will compete for the ultimate
prize!

What's your name contestant?""")

    contestant_name = input('Input contestant name: \n')
    
    print(f"\nWelcome {contestant_name}!!!!\n")
    input('<Press any key to continue>\n')
    
    print(f"I'd like to get to know you better {contestant_name}.")
    country = input("Where are you from? \n>")
    hate_food = input("What is a food that you don't like? \n> ")
    
    print(f"""
Ladies and gentlemen, this is {contestant_name},
Our contestant tonight is from {country},
and does not like {hate_food}.
We'll be right back after these messages from our sponsors.\n""")

    input('<Press any key to continue>\n')
    
    round_1()
    

def round_1():
    print(f"{host_name}: Welcome back to THE ULTIMATE GAMESHOW!")
    input('<Press any key to continue>\n')
    print(f"""
{host_name}: Our first round is Heads or Tails!

{host_name}: In this round, {contestant_name} will try to guess whether
             or not a coin lands on heads or tails. {contestant_name}
             will have two chances on two seperate flips. Let's get
             started!!!
             
""")
    input('<Press any key to continue>\n')

    chances = 2
    
    while chances > 0:
        flip_value = randint(0, 1)
        print(f"""
{host_name}: {contestant_name}, what's your guess?
             1) heads
             2) tails

""")
        coin = input("> ")
        
        if "1" in coin or "heads" in coin:
            if flip_value == 0:
                print(f"""
{host_name}: That's correct! You're amazing {contestant_name}!!!

""")
                input('<Press any key to continue>\n')
                round_2()
                break
            
            else:
                print(f"""
{host_name}: Oh, I'm sorry {contestant_name}, that's incorrect.

""")
                chances -= 1

        elif "2" in coin or "tails" in coin:
            if flip_value == 1:
                print(f"""
{host_name}: That's correct! You're amazing {contestant_name}!!!

""")
                input('<Press any key to continue>\n')
                round_2()
                break
            
            else:
                print(f"""
{host_name}: Oh, I'm sorry {contestant_name}, that's incorrect.

""")
                chances -= 1
    
    fail()

def round_2():
    print(f"""{host_name}: Our second round is Guess the Suit!

{host_name}: In this round, {contestant_name} will try to guess the
             suit in a deck of 52 cards. {contestant_name} will have
             three chances on three seperate draws. Let's get started!!
             
""")
    input('<Press any key to continue>\n')

    chances = 3
    
    while chances > 0:
        suit_value = randint(0, 3)
        print(f"""
{host_name}: {contestant_name}, what's your guess?
             1) hearts
             2) diamonds
             3) clubs
             4) spades

""")
        suit = input("> ")
        if "1" in suit or "heart" in suit:
            if suit_value == 0:
                print(f"""
{host_name}: That's correct! You're amazing {contestant_name}!!!

""")
                input('<Press any key to continue>\n')
                round_3()
                break
            
            else:
                print(f"""
{host_name}: Oh, I'm sorry {contestant_name}, that's incorrect.

""")
                chances -= 1


        elif "2" in suit or "diamonds" in suit:
            if suit_value == 1:
                print(f"""
{host_name}: That's correct! You're amazing {contestant_name}!!!

""")
                input('<Press any key to continue>\n')
                round_3()
                break
            
            else:
                print(f"""
{host_name}: Oh, I'm sorry {contestant_name}, that's incorrect.

""")
                chances -= 1


        elif "3" in suit or "clubs" in suit:
            if suit_value == 2:
                print(f"""
{host_name}: That's correct! You're amazing {contestant_name}!!!

""")
                input('<Press any key to continue>\n')
                round_3()
                break
            
            else:
                print(f"""
{host_name}: Oh, I'm sorry {contestant_name}, that's incorrect.

""")
                chances -= 1


        elif "4" in suit or "spades" in suit:
            if suit_value == 3:
                print(f"""
{host_name}: That's correct! You're amazing {contestant_name}!!!

""")
                input('<Press any key to continue>\n')
                round_3()
                break
            
            else:
                print(f"""
{host_name}: Oh, I'm sorry {contestant_name}, that's incorrect.

""")
                chances -= 1

            fail()


def round_3():
    print(f"""
{host_name}: Our FINAL ROUND is Mystery Door!

{host_name}: In this round, {contestant_name} will select one of three
             doors. Behind each door is one of three items:
                 * a giant bowl of {hate_food.upper()}!
                 * an even more giant bowl of {hate_food.upper()}!
                 * the ULTIMATE tour of Hult San Francisco campus!
             
""")

    input('<Press any key to continue>\n')

    print(f"""
{host_name}: Choose wisely {contestant_name},
             all of {country} is watching!

             1) Door 1
             2) Door 2
             3) Door 3
    
""")

    door = int(input('> '))
    prize_door = randint(0, 2)
    
    if door == prize_door:
        print(f"""
{host_name}: Oh my goodness {contestant_name}! I can't believe you won
             the ultimate prize of an ULTIMATE tour of Hult San
             Francisco campus! Enjoy it!
             
""")

        input('<Press any key to exit>\n')
        exit(0)
    
    else:
        print(f"""
{host_name}: Enjoy your {hate_food} {contestant_name}!
""")
        fail()





def fail():
    print(f"""
{host_name}: Oh, I'm sorry {contestant_name}, looks like you've lost
             in THE ULTIMATE GAMESHOW.
             
""")
    
    print(f"{host_name}: Would you like to play again? (Yes/No)")
    replay = input("> ")
    replay = replay.lower()
    
    if replay == 'yes':
        round_1()
        
    else:
        print(f"{host_name}: Thanks for playing {contestant_name}!")
        exit(0)


###############################################################################
# Game Start
###############################################################################
game_start()
