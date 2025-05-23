def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current = "X"

    print("🎮 Tic Tac Toe (2 Players)")
    print_board(board)

    while True:
        try:
            move = input(f"\nPlayer {current}, enter row and col (0 1): ").split()
            row, col = int(move[0]), int(move[1])
            if board[row][col] != " ":
                print("❗Cell already taken!")
                continue
            board[row][col] = current
            print_board(board)

            if check_win(board, current):
                print(f"🏆 Player {current} wins!")
                break
            if is_full(board):
                print("🤝 It's a tie!")
                break

            current = "O" if current == "X" else "X"
        except:
            print("⚠️ Invalid input. Try again.")

if __name__ == "__main__":
    main()
