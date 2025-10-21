# Simple Tic-Tac-Toe

board = [" "]*9

def print_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-+-+-")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-+-+-")
    print(board[6]+"|"+board[7]+"|"+board[8])

player = "X"
for i in range(9):
    print_board()
    move = int(input(f"Player {player}, choose 1-9: ")) - 1
    if board[move] == " ":
        board[move] = player
    else:
        print("Already taken, try again.")
        continue
    player = "O" if player == "X" else "X"

print_board()
print("Game Over!")
