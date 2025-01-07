import random

chances = 0
x = random.randint(1, 100)
print("You have 5 chances to guess the number from 1 to 100!")

b = True
while b == True:
    try:
        guess = input("Guess the number from 1 to 100: ")
        int_guess = int(guess)
        if x == int_guess:
          print("You are correct the number is", x)
          b = False
          chances = chances + 1
          print("You guessed the correct answer with only", chances, "attempt")
        elif int_guess > x: 
          chances = chances + 1 
          print("The number is smaller than your guess. You have", 5-chances, "left!") 
          if chances == 5:
            b = False
            print("You have failed! The correct is", x)
        elif int_guess < x:
          chances = chances + 1 
          print ("The number is bigger than your guess. You have", 5-chances, "left!") 
          if chances == 5:
            b = False
            print("You have failed! The correct is", x)
    except:
     print("Error! Incorrect input!")
     
