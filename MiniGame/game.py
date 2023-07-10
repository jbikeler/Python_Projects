#Python -V: 3.11.4
#
#Author: Ben Ikeler
#
#Purpose: Tech Academy - learn python
#
from playsound import playsound #need to use playsound 1.2.2 NOT 1.3

def start(nice=0,mean=0,name=''):
    #get the user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
    Check o see if his is a new game or not.
    If i is new, ge he user's name.
    If it is not a new game, thank the
    player for playing it again and continue with the game.
    """
    #meaning, if we do not already have this users name,
    #then they are a new player and we need to get their name
    if name != "":
        print("\nThank your for playing again {}!.".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input('\nWhat is your name? \n>>>').capitalize()
                if name != "":
                    print('\nWelcome, {}!'.format(name))
                    print('\nIn this scheme you will be greeted \nby several different people. \nYou can choose to be nice or mean.')
                    print('But, at the end of the game, your fate \nwill be sealed by your actions.')
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a conversation. Will you be nice \nor mean? (N/M) /n>>>').lower()
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass 3 variables to the score()
    
def show_score(nice,mean,name):
    print('\n{}, your current total: \n({}, Nice) and ({}, Mean)'.format(name, nice, mean))

def score(nice,mean,name):
    #score function is being passed the values stored within the # variables
    if nice > 2: #If the condition is valid, call win function passing the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #If the condition is valid, call lose function passing the variables so it can use them
        lose(nice,mean,name)
    else: #Else, called nice/mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    #play win sound (using playsound modual)
    playsound('media/winGame.mp3')
    #Substitute the wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've made lots of friends along the way!".format(name))
    #Call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #play lose sound (using playsound modual)
    playsound('media/tie.mp3')
    #Substitute the wildcards with our variable values
    print("\nAhhhhhh too bad {} you lost! \nChange yo ways dawg!!!".format(name))
    #Call again function and pass in our variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)


if __name__ == "__main__":
    start()
