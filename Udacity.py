#  CODE REFACTORED INTO THE VARIOUS FUNCTIONS
#  def intro():
#     #introduction
# def print_pause():
# # pause

# def cave():
# Things that happen to the player goes in the cave
#  def field():
#     # Things that happen when the player runs back to the field

# def house():
#     pycodestyle Udacity.pyThings that happen to the player in the house
# def play_again():


import time
import random


items = []
enemy = random.choice(["wicked fairie", "pirate", "troll",
                       "gorgon"])


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(enemy):
    print_pause("You find yourself standing in an open field,"
                " filled with grass,and yellow wildflowers")
    print_pause("Rumor has it that a " + enemy + " is somewhere "
                " around here and has been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def field(items, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    room = input("please enter 1 or 2\n")
    if room == '1':
        house(items, enemy)
    elif room == '2':
        cave(items, enemy)


def cave(items, enemy):
    # Things that happen to the player goes in the cave
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        field(items, enemy)
    elif "sword" not in items:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and"
                    " take the sword with you.")
        print_pause("You walk back out to the field.\n")
    items.append("sword")
    field(items, enemy)


def house(items, enemy):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and"
                " out steps a " + enemy + ".")
    print_pause("Eep! This is the " + enemy + 's' + " house!")
    print_pause("The " + enemy + " attacks you!")
    if "sword" in items:
        response2 = input("Would you like to (1) fight or (2) run away?")
        if response2 == "1":
            print_pause("As the " + enemy + " moves to attack,"
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly"
                        " in your hand as you brace yourself for the attack.")
            print_pause("But the " + enemy + " takes one look at"
                        " your shiny new toy and runs away!")
            print_pause("You have rid the town of the " + enemy +
                        " .You are victorious!")
            play_again()
        elif response2 == "2":
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been followed.\n")
            field()
    elif "sword" not in items:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
        response2 = input("Would you like to (1) fight or (2) run away?")
        if response2 == "1":
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the dragon.")
            print_pause("You have been defeated!")
            play_again()
        elif response2 == "2":
            print_pause("You run back into the field. Luckily,"
                        " you don't seem to have been followed.\n")
            field(items, enemy)


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.")


def play_game():

    intro(enemy)
    field(items, enemy)


play_game()
