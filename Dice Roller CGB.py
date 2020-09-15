import random


def mainMenu():  #defines mainMenu module below
    print ("*" * 30)  #design
    print ("Program 4: The Dice Roller")  #Make intro to show what Program this is
    print ("*" * 30)  #design x2
    print ("Welcome to the dice roller program!  Here are your options:")  #welcomes user to program and tell them what's coming next



def main():  #defines main module below
    choice = 1  #Design variable

    mainMenu() #Display main menu
    while choice != 0:  #makes while loop to print the categories while choice does not equal 0
        print("1.) 4 sided dice \n2.) 6 sided dice \n3.) 8 sided dice \n4.) 10 sided dice \n5.) 20 sided dice \n0.) Exit \n") #displays info
        choice = int(input())  #allows user to input which dice they want to roll
        

        exitToMain = 'n'  #create exitToMain variable and set equal to 'n'
        while exitToMain != 'y':  #create while loop to run unless exitToMain is 'y'
            if choice == 1:  #if choice from main menu equals 1, then the following will execute
                fourSided = random.randrange(1,5)  #assigns variable from random library to create a range of 1-4
                print (fourSided)  #prints the random number generated
                if fourSided == 1: #if variable generates number equal to 1 (smallest number)
                        print ("Min roll! Try again!")  #executes statement for above if statement
                elif fourSided == 4:  #if variable generates number equal to 4 (largest number)
                        print ("Congrats! Max roll!")  #executes statement for above elif statement
                else:  #if none of the above statements are true...
                        print ("Good roll!")  #print this

                        
            elif choice == 2:  #if choice from main menu equals 2, then the following will execute
                sixSided = random.randrange(1,7)  #siigns variable from random library to create a range of 1-6
                print (sixSided)  #prints the random number generated
                
                if sixSided == 1:  #if variable generates number equal to 1 (smallest number)
                        print ("Min roll! Try again!")  #executes statement for above if statement
                elif sixSided == 6:  #if variable generates number equal to 6 (largest number)
                        print ("Congrats! Max roll!")  #executes statement for above elif statement
                else:  #if none  of the above statements are true...
                        print ("Good roll!")  #print this

                        
            elif choice == 3:  #Rinse and repeat with an eight-sided dice
                eightSided = random.randrange(1,9)
                print (eightSided)
                if eightSided == 1:
                        print ("Min roll! Try again!")
                elif eightSided == 8:
                        print ("Congrats! Max roll!")
                else:
                        print ("Good roll!")

                
            elif choice == 4:  #Rinse again and repeat again with a ten-sided dice
                tenSided = random.randrange(1,11)
                print (tenSided)
                if tenSided == 1:
                        print ("Min roll!  Try again!")
                elif tenSided == 10:
                        print ("Congrats! Max roll!")
                else:
                        print ("Good roll!")


            elif choice == 5:  #then again with a twenty-sided dice
                twentySided = random.randrange(1,21)
                print (twentySided)
                if twentySided == 1:
                        print ("Min roll!  Try again!")
                elif twentySided == 20:
                        print ("Congrats! Max roll!")
                else:
                        print ("Good roll!")


            elif choice == 0: #if the choice from the main menu equals 0, then the following will execute
                exitToMain = 'y'  #sets variable to 'y'
                break  #break loop


            exitToMain = input("Exit to main menu? Y/N: ").lower()  #input to ask user if they want to exit to menu

    # End Of Program
    print ("Thank you for using the dice roller! \nThanks and play again!")

    
# Call to the main function to start the program
main()
