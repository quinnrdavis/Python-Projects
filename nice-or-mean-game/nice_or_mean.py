#
# Python: 3.10.5
#
# Author: Quinn R. Davis
#
# Purpose: The Tech Academy - Python Course, creating my first
#          text-based game with Python

# global variable to hold whether most recent finished game was won or lost, and customize quit messages based on that
nice_or_mean = 0

def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the player
        for playing again and continue with the game
    """
    if name != "":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>: ").capitalize()
                if name != "":
                    print("\nWelcome, {}".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \n You can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


# prompt user if they want to be nice or mean
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and stomrs off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name)

# display score to screen
def show_score(nice,mean,name):
    print ("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

# if nice or mean hit 3, call winning or losing functions, otherwise keep playing
def score(nice,mean,name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

# tell the user they've won and ask if they want to play again
def win(nice,mean,name):
    # store that most recent game was won so quit message can be customized
    global nice_or_mean
    nice_or_mean = 1
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name)

# tell the user they've lost and ask if they want to play again
def lose(nice,mean,name):
    # store that most recent game was lost so quit message can be customized
    global nice_or_mean
    nice_or_mean = 2
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>: ".lower())
        # if user says yes, reset game
        if choice == "y":
            stop  = False
            reset(nice,mean,name)
        # if no, quit game
        if choice == "n":
            if nice_or_mean == 1:
                print("\nEveryone will miss you, good luck.")
                stop = False
                quit()
            if nice_or_mean == 2:
                print("\nGood riddance, everyone is glad to see you leave.")
                stop = False
                quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>: ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # don't reset the name because it is the same user
    start(nice,mean,name)
            



if __name__ == "__main__":
    start()
