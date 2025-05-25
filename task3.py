import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board, revealed):
    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            if revealed[i][j]:
                row += f" {board[i][j]} "
            else:
                row += " * "
        print(row)
    print()

def create_board(size=4):
    symbols = [chr(65 + i) for i in range((size * size) // 2)] * 2
    random.shuffle(symbols)
    board = []
    for i in range(size):
        board.append([symbols.pop() for _ in range(size)])
    return board

def play_game(time_limit=60):
    size = 4
    board = create_board(size)
    revealed = [[False]*size for _ in range(size)]
    matched_pairs = 0
    total_pairs = (size * size) // 2
    start_time = time.time()

    while matched_pairs < total_pairs and (time.time() - start_time) < time_limit:
        clear_screen()
        print_board(board, revealed)
        print(f"Time left: {int(time_limit - (time.time() - start_time))} seconds")

        try:
            x1, y1 = map(int, input("Enter coordinates of first card (row col): ").split())
            x2, y2 = map(int, input("Enter coordinates of second card (row col): ").split())
        except:
            print("Invalid input. Please enter two numbers.")
            time.sleep(1)
            continue

        if (x1 == x2 and y1 == y2) or not (0 <= x1 < size and 0 <= y1 < size and 0 <= x2 < size and 0 <= y2 < size):
            print("Invalid coordinates. Try again.")
            time.sleep(1)
            continue

        revealed[x1][y1] = True
        revealed[x2][y2] = True
        clear_screen()
        print_board(board, revealed)

        if board[x1][y1] == board[x2][y2]:
            print("Matched!")
            matched_pairs += 1
        else:
            print("Not a match!")
            time.sleep(2)
            revealed[x1][y1] = False
            revealed[x2][y2] = False

    clear_screen()
    if matched_pairs == total_pairs:
        print("🎉 Congratulations! You matched all pairs in time!")
    else:
        print("⏱️ Time's up! Game over.")
    print_board(board, [[True]*size for _ in range(size)])

# Start the game
play_game(time_limit=60)
