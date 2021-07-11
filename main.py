import random
from logo import logo

def set_difficulty():
  level = input ("What level would you like to play: easy, medium, or hard? ")
  print("I'm thinking of a number between 1 and 100")

  if level == "easy":
    return 10
  elif level == "medium":
    return 7
  else:
    return 5

def check_guess(answer,guess,guesses):
  if guess > answer:
      print("Too high")
  elif guess < answer:
      print("Too low")
  else:
    print("You got it!")
  return guesses - 1


def game():
  print(logo)
  print ("Welcome to the number guessing game")
  number = random.randint(1,100)
  guesses = set_difficulty()
  guess = 0

  while guesses > 0 and guess != number:
    print(f"You have {guesses} guesses left")
    guess = int(input("What number am I thinking of? "))
    guesses = check_guess(number, guess, guesses)
    if guesses == 0:
      print("You've lost")

game()
    
  



