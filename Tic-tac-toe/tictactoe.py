import os
from helpers import check_turn, check_for_win, draw_board

# Declare all the variables we're going to need
spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}
playing, complete = True, False
turn = 0

# Game Loop
while playing:
    # Reset the screen
    os.system('clear')
    # Draw the current Game Board
    draw_board(spots)
    print('Pick your spot or press q to quit')
    
    # Get input and make sure it's valid
    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
      turn += 1
      spots[int(choice)] = check_turn(turn)
      
    # Check someone has won
    if check_for_win(spots): playing, complete = False, True
    
# Update the board one last time. If there was a winner, say who won
os.system('clear')
draw_board(spots)
if complete:
  if check_turn(turn) == 'X': print("Player One Wins!")
  else: print("Player Two Wins!")
  
print("Thanks for playing")