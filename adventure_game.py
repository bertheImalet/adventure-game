import time
import random
import sys
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)


villain = random.choice(["pirate", "dragon", "gorgon"])


def valid_input(prompts):
    while True:
        for prompt in prompts:
            print_pause(prompt)
        choice = input("(Please enter 1 or 2)")
        if choice == '1':
            return '1'
        elif choice == '2':
            return '2'
        else:
            print_pause("Please enter 1 or 2")


def intro():
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers")
    print_pause("Rumor has it that")
    print_pause("a " + villain + " is somewhere around here,")
    print_pause("and has been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty")
    print_pause("(but not very effective) dagger")


def field(items):
    choice = valid_input(["Enter 1 to knock on the door of the house",
                          "Enter 2 to peer into the cave.",
                          "What would you like to do?"])
    if choice == '1':
        house(items)
    elif choice == '2':
        cave(items)


def cave(items):
    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before")
        print_pause("and gotten all the good stuff")
        print_pause("It's an empty cave now.")
        print_pause("You walk back to the field")
        field(items)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger")
        print_pause("and take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("sword")
        field(items)


def house(items):
    print_pause("You approach the door of the house")
    print_pause("You are about to knock when")
    print_pause("the door opens and out steps a " + villain + ".")
    print_pause("Eep! This is the " + villain + " 's house!")
    print_pause("The " + villain + " attacks you!")

    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this,")
        print_pause("what with only having a tiny dagger.")

    second_choice = valid_input(["Would you like to (1)"
                                 "fight or (2) run away?"])
    if second_choice == '1':
        if "sword" in items:
            print_pause("As the " + villain + " moves to attack")
            print_pause("you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines")
            print_pause("brightly in your hand")
            print_pause("as you brace yourself for the attack.")
            print_pause("But the " + villain + " takes one look")
            print_pause("at your shiny new toy and runs away!")
            print_pause("You have rid the town of the pirate.")
            print_pause("You are victorious!")
            play_again()

        else:
            print_pause("You do your best...")
            print_pause("but your dagger")
            print_pause("is no match for the pirate.")
            print_pause("You have been defeated!")
            play_again()

    elif second_choice == '2':
        print_pause("You run back into the field.")
        print_pause("Luckily,")
        print_pause("you don't seem to have been followed.")
        field(items)


def play_again():
    user_choice = valid_input(["Would you like to play again? (1) yes (2) no"])
    if user_choice == '1':
        global villain
        villain = random.choice(["pirate", "dragon", "gorgon"])
        global items
        items = []
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif user_choice == '2':
        print_pause("Thanks for playing! See you next time.")
        sys.exit()


def play_game():
    intro()
    items = []
    field(items)


play_game()
