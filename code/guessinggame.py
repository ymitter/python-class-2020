import random
the_number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10 : "))
while guess != the_number:
    if guess > the_number:
        print(guess, "was to high. try again.")
    if guess < the_number:
        print(guess, "was to low. try again.")
    guess = int(input("Guess again: "))
print(guess, "was the number! You win!")   
        
    
