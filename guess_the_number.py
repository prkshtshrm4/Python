import random #imprt the library
print("Guess The Number \nBy Parikshit Sharma (2K18CSUN01121) \nAnd Ravi Prakash (2K18CSUN01127")
print("<-------------------------------------------------Game Rules--------------------------------------------------------------------------->")
print("Step 1 : Enter Your Range from min and max Range  \nStep2 : Enter number of chances you want to , guess the number     \nStep3 : Guess the number under Step 2 chances other wise you will Lose ")
kamsekam = int(input("Enter Minimum Range : ")) # Min range input taken
zadasezada = int(input("Enter Maximum Range : ")) # Max range input taken
if kamsekam >= zadasezada:
    print("Min Valur Cannot be greater than equal to Max Value")
    exit
else:
    baari = int (input("Enter your desired number of chances :")) # No. Of chances Reqired by us
    number = random.randint(kamsekam, zadasezada) # Here We have Defined the range of random number to be genrated
    chances = 0 # This is our Chance counter
    print("Guess a number between", kamsekam, "and", zadasezada, "Under", baari, "chances")
    while chances < baari: # Conditional Case Says while We are not exceeding no. of chances we can enter the more numbvers.
        print("Guess Counter: ", chances, "/", baari)
        guess = int(input("Enter your Guess: "))
        if guess == number: #If guess is correct theprint this
            print("Badhaiyaan Aap Jeet Gae \nCongratulation you have Won !!! ") # Print Cse If Player Wins
            break
        elif guess < number: # If Your Entered number is lower than actual number
            print("Try guessing a number higher than", guess)
        else: #If your Guessed number is Higher than actual number
            print("Try guessing a number lower than", guess)
        chances += 1
    if not chances < baari: # If your cannces exeet chance limit You Lose
        print("!!!YOU LOSE!!! The correct number is", number) # Print CAse If Player Losses5
