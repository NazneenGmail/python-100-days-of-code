import random
import ASCII_Art_RockPaperScissors

print("""
Welcome to Rock-Paper-Scissors Game
    Type 0 for Rock
    Type 1 for Paper
    Type 2 for Scissors\n
""")
user_choice = int(input("What do you choose? ==> "))
computer_choice = random.randint(0,2)
print("Your choice is: ")
ASCII_Art_RockPaperScissors.print_ascii_art_rock_paper_scissors(user_choice)
print("Computer choice is : ")
ASCII_Art_RockPaperScissors.print_ascii_art_rock_paper_scissors(computer_choice)

if user_choice == 0 and computer_choice == 1:
    print("Computer wins")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins")
elif user_choice == 1 and computer_choice == 2:
    print("Computer wins")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == computer_choice:
    print("It is a draw")
else:
    print("You typed an invalid input. You lose!")