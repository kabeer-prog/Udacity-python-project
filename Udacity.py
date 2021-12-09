import time
import random

tool = []
enemy = random.choice(["wicked fairie", "pirate", "troll",
                       "gorgon"])


def print_pause(message):
    print(message)
    time.sleep(2)


def introduction(tool, enemy):
    print_pause("You find yourself standing in an",
                " open field,filled with grass",
                " and yellow wildflowers")
    print_pause("Rumor has it that a " + enemy +
                " is somewhere around here and has",
                " been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def field(tool, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    response = input("(please enter 1 or 2)\n")
    while True:
        if response == "1":
            house(tool, enemy)
        elif response == "2":
            cave(tool, enemy)
        break


def house(tool, enemy):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door",
                "opens and out steps a " + enemy + ".")
    print_pause("Eep! This is the " + enemy + 's' + " house!")
    print_pause("The " + enemy + " attacks you!")
    if "sword" not in tool:
        print_pause("You feel a bit under-prepared for this,"
                    "what with only having a tiny dagger.")
        response1 = input("Would you like to (1) fight or (2) run away?\n")
    while True:
        if response1 == "1":
            if "sword" not in tool:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the ",
                            + enemy + ".")
                print_pause("You have been defeated!")
                play_again()
        if "sword" in tool:
            print_pause("\nAs the " + enemy + " moves to attack, "
                        "you unsheath your new sword.")
            print_pause("\nThe Sword of Ogoroth shines brightly in "
                        "your hand as you brace yourself for the "
                        "attack.")
            print_pause("\nBut the " + enemy + " takes one look at "
                        "your shiny new toy and runs away!")
            print_pause("\nYou have rid the town of the " + enemy +
                        ". You are victorious!\n")
            play_again()
        if response1 == "2":
            print_pause("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            field(tool, enemy)
        break


def cave(tool, enemy):
    if "sword" in tool:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nYou've been here before, and gotten all",
                    " the good stuff. It's just an empty cave",
                    " now.")
        print_pause("\nYou walk back to the field.\n")
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nIt turns out to be only a very small cave.")
        print_pause("\nYour eye catches a glint of metal behind a "
                    "rock.")
        print_pause("\nYou have found the magical Sword of Ogoroth!")
        print_pause("\nYou discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("\nYou walk back out to the field.\n")
        tool.append("sword")
    field(tool, enemy)


def play_again():
    print_pause("GAME OVER")
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    introduction(tool, enemy)
    field(tool, enemy)


play_game()
