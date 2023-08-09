import os
from helpers import check_turn, check_for_win, draw_board, boot_turn

# Declare all the variables we're going to need
devMode = False
spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',  8: '8', 9: '9'}
playing, complete, play_with_boot = True, False, bool()
turn = 0
prev_turn = -1
#Choose the type of match
print("Choose the type of match you want.")
print("1. Boot")
print("2. PVP")
play_with_boot = True if int(input()) == 1 else False

# Game Loop
while playing:
    # Reset the screen
    if devMode == False:
        os.system('cls' if os.name == 'nt' else 'clear')
    # Draw the current Game Board
    draw_board(spots)
    # If an invalid turn occurred, let the player know
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press q to quit")


    if play_with_boot & turn % 2 != 0: 
        boot_turn(spots, turn,devMode)
        turn += 1
    else:
        choice = input()
        # The game has ended,
        if choice == 'q':
            playing = False
        elif str.isdigit(choice) and int(choice) in spots:
            # Check if the spot is already taken.
            if not spots[int(choice)] in {"X", "O"}:
                # If not, update board and increment the turn
                spots[int(choice)] = check_turn(turn)
                turn += 1
    # Check if the game has ended (and if someone won)
    if check_for_win(spots):
        playing, complete = False, True
    if turn > 8:
        playing = False
# Update the board one last time.
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
# If there was a winner, say who won
if complete:
    if check_turn(turn) == 'O':
        print("Player 1 Wins!")
    else:
        if play_with_boot :
            print("The robot has won!")
        else:
            print("Player 2 Wins!")
else:
    # Tie Game
    print("No Winner")

print("Thanks for playing!")
