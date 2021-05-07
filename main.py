import random
def print_pattern(choice):
  rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''

  paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
          _______)
  ---.__________)
  '''

  scissors = '''
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  '''
  game_images = [rock, paper, scissors]
  print(game_images[choice])
  
def result(n1,n2):
  if n1==n2:
    print("It's a draw")
  elif n1 == 0:
    if n2 == 1:
      print("You lose")
    else:
      print("You win!")
  elif n1 == 1:
    if n2 == 2:
      print("You lose")
    else:
      print("You win!")
  elif n1 == 2:
    if n2 == 0:
      print("You lose")
    else:
      print("You win!")

if __name__ == "__main__":
  choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  print_pattern(choice)
  computer=random.randint(0,2)
  print("Computer chose:")
  print_pattern(computer)
  result(choice,computer)
