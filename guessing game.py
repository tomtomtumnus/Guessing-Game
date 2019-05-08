import random
import time

rand = random.randint(1,50)

print("I am thinking of a number between 1 and 50.")

time.sleep(1)

print("Can you guess what it is?")

time.sleep(1)

def read_int(prompt):
  while True:
    value = input(prompt)
    try:
      return int(value)      
    except ValueError:
      print("That's not a number!")
  guess = read_int("Your Guess: ")

def read_guess_again(prompt):
  answer = ("no", "n", "yes","y")
  while True:
    again = input(prompt)
    if again not in answer:
      print('This is a yes or no question...')
    elif again in answer:
      return again

while True:
  guess = read_int("Your Guess: ")
  if guess == rand:
    print("Congratulations! That is correct.")
    break
  elif guess > rand:
    print("I'm sorry, your guess was incorrect! Your number is too high.")
    guess_again = read_guess_again("Would you like to guess again? ")
    if guess_again not in ("yes","y"):
      break
  else:
    print("I'm sorry, your guess was incorrect! Your number is too low.")
    guess_again = read_guess_again("Would you like to guess again? ")
    if guess_again not in ("yes","y"):
      break
