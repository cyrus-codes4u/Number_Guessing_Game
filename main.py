import random
# Include an ASCII art logo.


level = input ("What level would you like to play: easy, medium, or hard? ")
print("I'm thinking of a number between 1 and 100")


if level == "easy":
  guesses = 10
elif level == "medium":
  guesses = 7
else:
  guesses = 5

number = random.randint(1,100)
correct = False

while guesses > 0 and correct == False:
  print(f"You have {guesses} guesses left")
  guess = int(input("What number am I thinking of? "))
  guesses = guesses - 1
  if guess == number:
    print("You got it!")
    correct = True
  else:
    if guesses == 0:
      print("You lost")
    elif guess > number:
      print("Too high")
    else:
      print("Too low")
