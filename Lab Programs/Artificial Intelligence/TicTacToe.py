import random

# Board
b = [" "] * 9

# Winning combinations
wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6)              # diagonals
]

# Check winner
def check(p):
    return any(b[a] == b[b_] == b[c] == p for a, b_, c in wins)

# Print board
def show():
    print(b[0:3])
    print(b[3:6])
    print(b[6:9])
    print()

# Game loop
while True:
    show()
    
    # Player move
    i = int(input("Move (0-8): "))
    if b[i] != " ":
        continue
    b[i] = "X"

    if check("X"):
        show()
        print("You win")
        break

    if " " not in b:
        show()
        print("Draw")
        break

    # AI move
    move = None

    # Try to win or block
    for p in ["O", "X"]:
        for j in range(9):
            if b[j] == " ":
                b[j] = p
                if check(p):
                    move = j
                b[j] = " "
                if move is not None:
                    break
        if move is not None:
            break

    # Otherwise pick center or random
    if move is None:
        if b[4] == " ":
            move = 4
        else:
            move = random.choice([j for j in range(9) if b[j] == " "])

    b[move] = "O"
    print("AI:", move)

    if check("O"):
        show()
        print("AI wins")
        break

    if " " not in b:
        show()
        print("Draw")
        break
