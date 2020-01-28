import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

<<<<<<< HEAD

quit = False
range = 100

while not quit:
    randomNumber = random.randint(1,range)
    count = 1
    number = -1
    while number != randomNumber:
        number = input("please guess a number between 1 and {}:".format(range))
        if not number.isdigit():
            print("please guess a number!")
        else:
            number = int(number)
            count = count + 1
            print("Sorry, you didn't get it right")
            if number > randomNumber:
                print("Too high!")
            elif number < randomNumber:
                print("Too low!")
    print("Good job")
    print("You guessed it in {} tries!".format(count))
    play_again = input("\nWould you like to play again (yes or no)? ")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True

print("\n\nThanks for playing! See you later!")      
=======
>>>>>>> d0433f7f29310914b40a5cdd2be0d6527a4a8eeb
