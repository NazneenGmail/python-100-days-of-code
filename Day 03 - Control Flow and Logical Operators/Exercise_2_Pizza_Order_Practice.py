print("Welcome to Python Pizza Delivery\n")
size = input("\nWhat size pizza do you want? S, M, L: ")
pepperoni = input("\nDo you want pepperoni on your pizza? Y or N : ")
extra_cheese = input("\nDo you want extra cheese? Y or N : ")

bill = 0
if size == 'S' or size == 's':
    bill += 15
elif size == 'M' or size == 'm':
    bill += 20
elif size == 'L' or size == 'l':
    bill += 25
else:
    print("\nYou chose the wrong input.")

if pepperoni == 'Y' or pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 2
    elif size == 'M' or size == 'm' or size == 'L' or size == 'l':
        bill += 3

if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 1

print(f"\nYou order bill is ${bill}")