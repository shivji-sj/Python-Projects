"""Creating a Random Number Guesser Program that will help you to do some fun. Take and enjoy it."""
import random,os 

print("""#################################################### 
    This is Number Gusser Game. 
    You can guess number using given 3 chance.
######################################################""")
print("\n\nYou have only 3 Chance.")
while True:
    
    # creating upper and lower limits to bound the value. Which mean user given values lies between upper and lower limit.
    print("\n---------------------------------------------" )
    lower_limit, upper_limit, =   int(input("Lower Limit : " )), int(input("Upper Limit : " )) 
    random_number = random.randint(lower_limit,upper_limit)
    print(f"######################################## \nYou have to choose a number between {lower_limit} and {upper_limit}")

    # Assigning a variable "chance" that help to counter the loop 
    chance = 0

    while chance < 3:
        chance += 1
        # taking input guess number from user
        print(f"\nChance {chance}")
        print("_____________________________________________")
        guess_num =  int(input("Guess Your Number : "))

        
        if guess_num == random_number:
            print(f"Congratulations, You did it. The number was {random_number}")  
            break

        elif guess_num > random_number:
            print("You guessed a large number") 

        elif guess_num < random_number:
            print("You guessed a small number")

        if chance == 3:
            print("You have ran out of your chance.")
            print(f"===============================\nThe number was, {random_number} \n===============================")
            print("Better Luck for Next Time.")
            break
  