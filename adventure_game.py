import time
import random
from urllib import response

dangers = ["bandit", "terrorist"]
danger = random.choice(dangers)
tools = []


def print_pause(message_to_print, pause=2):
    print(message_to_print)
    time.sleep(pause)


def intro():
    print_pause("You are travelling to the neighbouring country of Niger.")
    print_pause("You were filled with excitement about you visiting a " +
                "new place")
    print_pause("Unfortunately, your car broke down in a thick" +
                "forest where no one lives")
    print_pause("At the same time, this happens to be the dreadful " +
                "Sambisa Forest,"+"common with " + danger + " !")
    print_pause("You've got either of two decisions to save yourself " +
                "from the mess.")
    print_pause("1) Repair the car or \n 2) Stay and not make an effort")
    option()


def option():
    choice = valid_input("Enter stay or repair?", ["stay", "repair"])
    if (choice == "stay"):
        stay()
    elif (choice == "repair"):
        repair()


def stay():
    print_pause("You heard steps of someone running towards " +
                "the road from the forest")
    print_pause("Few minutes after, a man who appears to be a captive of " +
                danger + ", came ot of the forest ")
    print_pause("He mentioned he was kidnaped by " +
                danger + " few weeks back.")
    print_pause("He wants your help from the " + danger + 's' + " attack")
    print_pause("Would you like to (1) wait and fight them " +
                "(2) hide away in the forest")
    choice2 = valid_input("Enter 1 or 2\n", ['1', '2'])
    if choice2 == "1" and "rifle" in tools:
        print_pause("As you waited for what will happen next")
        print_pause("You remembered the rifle you took from " +
                    "the boot moment before")
        print_pause("a soldier of " + danger + " appeared")
        print_pause("You shot the " + danger)
        print_pause("You are happy to save a life")
        one_more_time()
    elif choice2 == "1" and "rifle " not in tools:
        print_pause("A soldier of " + danger + " appeared")
        print_pause("He capture you")
        print_pause("You lost from the journey as you had nothing " +
                    "to save yourself")
        one_more_time()
    elif choice2 == "2":
        hide()


def hide():
    print_pause("You observed to know if it is safe to return to your car")
    print_pause("You took caution and was successful")
    one_more_time()


def repair():
    print_pause("You opened the bonnet")
    print_pause("You tried cautiously to examine the fault.")
    print_pause("it appears that an ignition plug is off " +
                "its position and needs to be tightened")
    print_pause("You need a spanner to do the job")
    print_pause("You proceeded to the boot of the car")
    boot()


def boot():
    print_pause("You open the boot in search of the spanner")
    if "spanner" in tools:
        print_pause("You've gotten the spanner ")
        print_pause("You went back to the car's bonnet\n")
        work()
    elif "spanner" not in tools:
        print_pause("As you were searching the tool box in the bonnet.")
        print_pause("You discovered a rifle youu bought, long time ago")
        print_pause("You took it, and placed it under your shirt in " +
                    "case of attack")
        print_pause("You also found the sppanner you are looking for")
    tools.append("spanner")
    tools.append("rifle")
    work()


def work():
    print_pause("You tightened the plug and it worked")
    stay()


def valid_input(prompt, options):
    response = input(prompt).lower()
    if response in options:
        return response
    else:
        print("Please select a correct input")
        return valid_input(prompt, options)


def one_more_time():
    play = valid_input("Would you like to go through the " +
                       "journey again (y/n)", ['y', 'n']).lower()
    if play == "n":
        print_pause("Thanks for your time!!! See you next time.")
    elif play == "y":
        print_pause("Restarting the game!!!! ...\n", 5)
        play_game()


def play_game():
    dangers = ["bandit", "terrorist"]
    danger = random.choice(dangers)
    tools = []
    intro()


play_game()
