
eggs_player1_start = int(input())
eggs_player2_start = int(input())

eggs_player1_current = eggs_player1_start
eggs_player2_current = eggs_player2_start

while eggs_player1_current >= 1 and eggs_player2_current >= 1:
    command = input()

    if command == 'End':
        print(f"Player one has {eggs_player1_current} eggs left.")
        print(f"Player two has {eggs_player2_current} eggs left.")
        #break
    elif command == 'one':
        eggs_player2_current -= 1

    elif command == 'two':
        eggs_player1_current -= 1
else:
    if eggs_player1_current == 0 and eggs_player2_current >= 1:
        print(f"Player one is out of eggs. Player two has {eggs_player2_current} eggs left.")
    elif eggs_player1_current >= 1 and eggs_player2_current == 0:
        print(f"Player two is out of eggs. Player one has {eggs_player1_current} eggs left.")
