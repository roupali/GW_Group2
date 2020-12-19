# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 00:36:53 2020

@author: Ephrem Fisahatsion 
PSIS_2105 Python Final Project
GWU
Professor Foster 

"""



from random import randint         # we will import the randint from random module  




def full_name(chosen):                  # full name function to check and set the name 
    if chosen == 1 or chosen == 'r' or chosen == 'R':       # conditional statement to check the parameter
        computer = 'rock'                                   # if the top condition is true set the variable 
    elif chosen == 2 or chosen == 'p' or chosen == 'P':     # conditional statement to check the parameter
        computer = 'paper'                                  # if the top condition is true set the variable
    elif chosen == 3 or chosen == 's' or chosen == 'S':     # conditional statement to check the parameter    
        computer = 'scissors'                               # if the top condition is true set the variable
    elif chosen == 4 or chosen == 'l' or chosen == 'L':     # conditional statement to check the parameter
        computer = 'lizard'                                 # if the top condition is true set the variable
    elif chosen == 5 or chosen == 'k' or chosen == 'K':     # conditional statement to check the parameter
        computer = 'spock'                                  # if the top condition is true set the variable
    else:
        computer = chosen

    return computer                                         # finaly return the value. 

def short_name(chosen):                                                  # short_name function is taking one argument and processes computer choice 
    if chosen == 1 or chosen == 'rock' or chosen == 'Rock':              # if the computer chose 1 then set it to 'r'
        computer = 'r'
    elif chosen == 2 or chosen == 'paper' or chosen == 'Paper':          # if the computer chose 2 then set it to 'p'
        computer = 'p'
    elif chosen == 3 or chosen == 'scissors' or chosen == 'Scissors':    # if the computer chose 3 then set it to 's'
        computer = 's'
    elif chosen == 4 or chosen == 'lizard' or chosen == 'Lizard':        # if the computer chose 4 then set it to 'l'
        computer = 'l'
    elif chosen == 5 or chosen == 'spock' or chosen == 'Spock':          # if the computer chose 5 then set it to 'k'
        computer = 'k'
    else:
        computer = chosen

    return computer                                                      # at the end return the result    

def get_winner_text(player, computer,a,b):                              # the get_winner_text holds 4 argument and process the game 
    
    if player == computer:                                              # if the computer and player choice is equal that means its a draw
        print('DRAW!')

    elif player == 'r' and computer == 's':                             # if player is rock and computer is scissor that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 'r' and computer == 'p':                             # if player is rock and computer is paper that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"
    elif player == 'r' and computer == 'l':                             # if player is rock and computer is lizard that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 'r' and computer == 'k':                             # if player is rock and computer is spock that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"

    elif player == 'p' and computer == 'r':                             # if player is paper and computer is rock that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 'p' and computer == 's':                             # if player is paper and computer is scissor that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"
    elif player == 'p' and computer == 'k':                             # if player is paper and computer is spock that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 'p' and computer == 'l':                             # if player is paper and computer is lizard that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"

    elif player == 's' and computer == 'p':                             # if player is scissor and computer is paper that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 's' and computer == 'r':                             # if player is scissor and computer is rock that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"
    elif player == 's' and computer == 'l':                             # if player is scissor and computer is lizard that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 's' and computer == 'k':                             # if player is scissor and computer is spock that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"

    elif player == 'l' and computer == 'p':                             # if player is lizard and computer is paper that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 'l' and computer == 's':                             # if player is lizard and computer is scissor that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"
    elif player == 'l' and computer == 'k':                             # if player is lizard and computer is spock that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 'l' and computer == 'r':                             # if player is lizard and computer is rock that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"

    elif player == 'k' and computer == 's':                             # if player is spock and computer is paper that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 'k' and computer == 'p':                             # if player is spock and computer is paper that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"
    elif player == 'k' and computer == 'r':                             # if player is spock and computer is rock that means player wins and return 'a'
        print('Player Wins!')
        return "a"
    elif player == 'k' and computer == 'l':                             # if player is spock and computer is lizard that means computer wins and return 'b'
        print('Computer Wins!')
        return "b"

    else:
        print("Wrong choice. Read instructions carefully." )           # if non of the above is correct, display the following message. 


            
def txt_file(name, w):                                          # txt_file function holding two parameters
    f = open("rpslk_2.txt", "a")                                # the following method help us open and append on the file
    f.write(str(w)+ ", " +str(name) + "\r\n"  )                 # the write method help us writing on the text file.
    #f.close()
    
    f = open ("rpslk_2.txt", "r")                               # open the file again to read
    readthefile = f.readlines()                                 # readline method help us the whole line
    sortedData = sorted(readthefile,reverse=True)               # the sort method help us the score to sort and reverse true meaning display from large to small
    
    print ("********Top 10 Scores**********")                   # display out put
    print ("Position\tPoints, Name")                            # display out put 
    
    
    for line in range(10):                                      # do the condition loop to look through 10 outputs 
                                        
        print(str(line+1)+"\t\t"+ str(sortedData[line]))        # print out the top 10 outputs 
        
        
    f.close()                                                   # we need to close the file 
    
    
    
def rpslk_instruction():                                        # the function that explain the rule about the game
    print()                                                     # only returns a print out ststement till the end 
    print("Instructions for Rock-Paper-Scissors-Lizard-Spock : ")
    print()
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    print()  
    
def display(game_played, p_win, c_win, name):                   # display function takes 4 argument 
    print("you played "+ str(game_played) + " Games.")          # prints out how many games played by the player
    print("You win: " + str(p_win)+ " Times.")                  # prints out how many times the player wins 
    print("Computer win: " + str(c_win)+ " Times.")             # prints out how many times the computer wins                 
    print("Thanks for playing. Good Bye!!")                     # prints good bye message
    print("")
    txt_file(name,p_win)                                        # it calls txt function and passes two argument 
    
def get_yes_or_no(message):                                     # to validate the user input we use this function 
    valid_input = False                                         # we set the variable to false 
    while not valid_input:                                      # we use conditional loop and set it to true
        answer = input(message)                                 # we prompt the user to enter the choice 
        answer = answer.upper()                                 # convert to upper case
        if answer == 'Y' or answer == 'N':                      # another if conditional statement to check the user input
            valid_input = True                                  # we set valid to true if the top condition is true
        else:
            print('Please enter Y for yes or N for no.')        # print out message 
    return answer                                               # return the result 
          
def main():                                                         # This is the main function and the program starts from here.                                     
    print()
    print ("Welcome to Rock, Paper, Scissor, Lizard and Spock Game!!")  # welcome message 
    print()
    name = input("Please Enter your Name: ")                        # prompt the user to enter the name 
    rpslk_instruction()                                         # call the rpslk function to display the rule of the game 
    game_played =0                                              # declare a variable and set a value 
    p_win = 0                                                   # declare a variable and set a value
    c_win = 0                                                   # declare a variable and set a value
    
    while True:                                                 # we will start a conditional function and set it to true 
        #game_played+=1
        print ("")
        print ("Please enter the following choice.")            # display message 
        print('For rock Enter (r), For scissors Enter (s), For paper Enter (p), For lizard Enter (l), or For spock Enter (k)') # instraction on how to choose the game 
        player = input('Enter choice:')                         # prompt the user to enter the choice 
        computer = randint(1,5)                                 # the randint function will randomely select b/n 1 -5 and convert it to integer 
        computer = short_name(computer)                         # wherever the computer selected, we pass it to short_name function (to set the name)
        player_choice = full_name(player)                       # wherever the user selected, we pass it to full name function (to set the name)
        computer_choice = full_name(computer)                   # also, werever we get from the computer choice, we pass it to full name function 
        
        options = ['r', 's', 'p', 'l', 'k']                     # we set a list of options 

        print('')
        
        if player in options:                                   # we do conditional function to go through the length of option list 
            vs_text = 'The Player chooses '+ player_choice + ' and ' + 'The computer chooses ' + computer_choice  
            print(vs_text)                                      # displayes the top out put. 
            
        game_played+=1                                          # increment every time play the game 
        a = ""                                                  # set an empty variable a         
        b = ""                                                  # set an empty variable b 
        r = get_winner_text(player, computer,a,b)               # call get_winner_text variable and pass 4 argument and the return hold it in r
        if r == "a":                                            # conditional statement to check the result value 
           p_win+=1                                             # if the top condition is true, increment the player win by 1         
        elif r == "b":
            c_win+=1                                            # else increment the computer win by one 
        
        playAgain = "play again? (y/n): "                       # a variable holds a message 
        get_result = get_yes_or_no(playAgain)                   # call get_yes_or_no function and pass the message       
        if get_result == 'Y':                       # conditional statement to check the user input
            continue                                                # if the top condition is true continue                                         
            game_played +=1                                         # increment the game_played variable 
                                                                    
        elif get_result == 'N':                 # if the top condition is true continue
            display(game_played, p_win, c_win, name)                # call the display function and pass 4 parameter   
            break                                                   # break and end the game
       
        
main()     

