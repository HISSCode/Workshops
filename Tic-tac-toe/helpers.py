def draw_board(spots):
  board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
  print(board)


def check_turn(turn):
  if turn % 2 == 0:
    return 'O'
  else: return 'X'

def check_for_win(dict):
  # Handle Horizontal Cases
  if   (dict[1] == dict[2] == dict[3]) \
    or (dict[4] == dict[5] == dict[6]) \
    or (dict[7] == dict[8] == dict[9]):
    return True
  # Handle Vertical Cases
  elif   (dict[1] == dict[4] == dict[7]) \
    or (dict[2] == dict[5] == dict[8]) \
    or (dict[3] == dict[6] == dict[9]):
    return True
  # Diagonal Cases
  elif (dict[1] == dict[5] == dict[9]) \
    or (dict[3] == dict[5] == dict[7]):
    return True
    
  else: return False