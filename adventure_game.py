import random
import time


def print_pause(text):
    print(text)
    time.sleep(2)


def intro():
    print_pause("You are in London.")
    print_pause("You are an undercover spy working for the govt of Genovia.")
    print_pause("Your mission is to save the city "
                "from a Genovian terrorist...")
    print_pause("...without the public and the UK govt finding out.")


def accept_mission():
    accept = input("Do you accept the mission?\n").lower()
    if accept == "yes":
        print_pause("You have accepted this mission!")
    elif accept == "no":
        print_pause("I'm sorry. You do not really have a choice..")
        print_pause("You have accepted the mission.")
    else:
        print_pause("Sorry, I do not understand. Please answer yes or no.")
        accept_mission()


def identity_choice():
    print_pause("You now need to choose your fake identity.")
    identity = input("Your options are:\n"
                     "1. Ordinary Tourist\n"
                     "2. Chef\n"
                     "3. Doctor\n"
                     "4. Ninja\n"
                     "Please choose a number\n").lower()
    if identity == "1":
        print_pause("Excellent! You now look like a tourist!")
        return identity
    elif identity == "2":
        print_pause("You now have a rather silly looking hat."
                    " But it could work")
        return identity
    elif identity == "3":
        print_pause("You now have a white coat and a stethoscope")
        return identity
    elif identity == "4":
        return identity
        print_pause("An odd choice for a smart spy. But oh well, here we go.")
        return identity
    else:
        print_pause("Sorry, I dont understand that. "
                    "Could you key in a number from 1 to 4?\n")
        return identity_choice()


def location():
    possible_locations = ["St Paul's Cathedral", "Kensington Gardens",
                          "Sushi Samba", "a homeless shelter"]
    location_choice = random.choice(possible_locations)
    print_pause("You have just received some intel from your handler.")
    print_pause(f"The terrorist is inside {location_choice}.")
    return location_choice


def alert_authority():
    print_pause("You call the cops.")
    print_pause("They search the terrorist and find a bomb.")
    print_pause("You have saved London but have failed your mission.")


def options_with_screwdriver():
    response = input("""What do you do?\n
    1. You alert the authorities.
    2. You take out your screwdriver to attack him. \n""").lower()
    if response == "1":
        alert_authority()
    elif response == "2":
        attack_with_screwdriver()
    else:
        print_pause("Sorry I don't understand. Choose 1 or 2. \n")
        options_with_screwdriver()


def options_without_screwdriver(identity):
    response = input("""What would you like to do?
    1. Attack him with your bear hands.
    2. Alert the authorities\n""").lower()
    if response == "1":
        if identity == "3":
            print_pause("You try and punch him.")
            print_pause("He takes out a knife to stab you.")
            print_pause("He is so close to killing you.")
            print_pause("Then the strangest thing happens.")
            print_pause("People start to notice a doctor")
            print_pause("Who they believe to have served "
                        "during the COVID-19 pandemic")
            print_pause("They rush to your rescue and kill the terrorist")
            print_pause("Your life if saved but you have failed your mission")
        else:
            attack_without_screwdriver()
    elif response == "2":
        alert_authority()
    else:
        print_pause("Sorry I don't understand. Choose 1 or 2.")
        options_without_screwdriver()


def attack_with_screwdriver():
    print_pause("You pull out your new screwdriver and stab him.")
    print_pause("You have killed him and have successfully "
                "completed your mission!")


def attack_without_screwdriver():
    print_pause("You try and punch him.")
    print_pause("He attacks you but you have nothing to defend yourself.")
    print_pause("You manage to run away and save yourself.")
    print_pause("But you have failed your mission and have lost the game.")


def action(identity, location_choice, items):
    action_one = input("What would you like to do next? You can: \n"
                       "1. Go find the terrorist at the location.\n"
                       "2. Go look for some tools to kill him with.\n"
                       "3. Quit the mission. You just want to go home. \n"
                       "Please choose a number.\n").lower()
    if action_one == "1":
        # tourist
        if identity == "1":
            print_pause("You find him.")
            print_pause("He thinks you're an ordinary tourist.")
            print_pause("He pays no attention to you")
            if "screwdriver" in items:
                options_with_screwdriver()
            else:
                options_without_screwdriver(identity)
        # chef
        elif identity == "2":
            print_pause("You find him")
            print_pause("He thinks you're an ordinary chef.")
            print_pause("He pays no attention to you")
            if "screwdriver" in items:
                options_with_screwdriver()
            else:
                options_without_screwdriver(identity)
        # doctor
        elif identity == "3":
            print_pause("You find him")
            print_pause("He thinks you're a doctor.")
            print_pause("He pays no attention to you")
            if "screwdriver" in items:
                options_with_screwdriver()
            else:
                options_without_screwdriver(identity)
        # ninja
        elif identity == "4":
            print_pause("You find him")
            print_pause("He is distracted by your disguise.")
            print_pause("He realises you're no ordinary ninja")
            while True:
                response = input("Would you like to change "
                                 "your disguise?\n").lower()
                if response == "yes":
                    identity = identity_choice()
                    action(identity, location_choice, items)
                    break
                elif response == "no":
                    print_pause("He attacks you")
                    if "screwdriver" in items:
                        attack_with_screwdriver()
                        break
                    else:
                        attack_without_screwdriver()
                        break
                else:
                    print_pause("Sorry I didn't understand. Please answer"
                                "with a yes or no.")
    elif action_one == "2":
        # tourist
        if identity == "1":
            if "screwdriver" in items:
                print_pause("You've got what you need from here.")
                action(identity, location_choice, items)
            else:
                print_pause("You go to the hardware store.")
                print_pause("You look around to see what can help "
                            "you kill a man")
                print_pause("You buy a screwdriver")
                items.append("screwdriver")
                action(identity, location_choice, items)
        # chef
        elif identity == "2":
            if "screwdriver" in items:
                print_pause("You've got what you need from here.")
                action(identity, location_choice, items)
            else:
                print_pause("You go to the hardware store")
                print_pause("They wonder why you need tools.")
                print_pause("You have no explanation but they sell you"
                            "a screwdriver anyway.")
                print_pause("It’s not illegal to buy a screwdriver.")
                items.append("screwdriver")
                action(identity, location_choice, items)
        # doctor
        elif identity == "3":
            if "screwdriver" in items:
                print_pause("You've got what you need from here.")
                action(identity, location_choice, items)
            else:
                print_pause("You go to the hardware store")
                print_pause("You pick out a screwdriver")
                print_pause("They ask if you’re going to use it in surgery.")
                print_pause("You jokingly say yes.")
                print_pause("They refuse to sell it to you")
                while True:
                    response = input("Would you like to change your "
                                     "disguise?. \nIf you do, you can go back "
                                     "to the hardware store."
                                     "for that screwdriver. \n").lower()
                    if response == "yes":
                        identity = identity_choice()
                        break
                    elif response == "no":
                        print_pause("You have left the store with no tools")
                        action(identity, location_choice, items)
                        break
                    else:
                        print_pause("Sorry I don't understand."
                                    "Please answer with yes or no")
        # ninja
        elif identity == "4":
            if "screwdriver" in items:
                print_pause("You've got what you need from here")
                action(identity, location_choice, items)
            else:
                print_pause("You’re welcomed in because they think"
                            "your outfit is cool.")
                print_pause("They give you a screwdriver for free.")
                items.append("screwdriver")
                action(identity, location_choice, items)
        else:
            print_pause("Sorry I don't understand")
            action(identity, location_choice, items)
    elif action_one == "3":
        print_pause("Okay, you decide not to save London.")
        print_pause(f"A bomb goes off at {location_choice}")
        print_pause("You have failed your mission")
    else:
        print_pause("Sorry, I don't understand")
        print_pause("Choose either 1, 2 or 3")
        action(identity, location_choice, items)


def play_again():
    while True:
        response = input("Would you like to play again?").lower()
        if response == "yes":
            play_game()
        elif response == "no":
            print("Goodbye!")
            break
        else:
            print("Sorry I don't understand")


def play_game():
    items = []
    intro()
    accept_mission()
    identity = identity_choice()
    location_choice = location()
    action(identity, location_choice, items)
    play_again()


play_game()
