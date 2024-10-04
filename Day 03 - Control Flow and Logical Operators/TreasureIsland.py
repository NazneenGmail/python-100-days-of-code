print("""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \..  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.\ U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.\ U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")
print("""
Welcome to Treasure Island.
Your mission, should you choose to accept, is to find the treasure.
""")
left_or_right = input("You are at a cross road. Where would you want to go? \n"
      "Type 'left' or 'right'\n").lower()
if left_or_right == 'left':
    print("You have come to a lake. There is an island in the middle of the lake.\n")
    wait_or_swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if wait_or_swim == 'wait':
        door_choice = input("Boat took you to a cave. Choose a door. "
                            "Type 'Red', 'Blue' or 'Yellow'\n").lower()
        if door_choice == 'red':
            print("Burned by fire. GAME OVER")
        elif door_choice == 'blue':
            print("Eaten by beast. GAME OVER")
        elif door_choice == 'yellow':
            print("YOU WIN")
        else:
            print(f"Wrong input : {door_choice}")
    else:
        print("Attacked by trout. GAME OVER")
else:
    print("You have fallen into a hole. GAME OVER.")