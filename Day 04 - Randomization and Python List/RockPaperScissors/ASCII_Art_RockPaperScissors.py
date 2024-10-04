# Rock Paper Scissors ASCII Art

# Rock
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def print_ascii_art_rock_paper_scissors(choice):
    if choice == 0:
        print("rock")
        print(rock_art)
    elif choice == 1:
        print("paper")
        print(paper_art)
    elif choice == 2:
        print("scissors")
        print(scissors_art)
    else:
        print("Wrong Choice")