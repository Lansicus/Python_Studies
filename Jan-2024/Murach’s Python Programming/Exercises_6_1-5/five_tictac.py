def main():
    print("Welcome to Tic Tac Toe")
    display_grid()
    start_game()


# ---------------------------------------------------------------------------------------------------------- GRID SET-UP
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]


def display_grid():
    print()
    print("+---+---+---+")
    for row in grid:
        print("|", end="")
        for column in row:
            print(f" {column} |", end="")
        print()
        print("+---+---+---+")
    print()


# ----------------------------------------------------------------------------------------------------- INITIALIZE TURNS
def start_game():
    game_over = False
    while not game_over:
        game_over = take_turn()
    print()
    print("Game over!")


def take_turn():
    turn = 1
    while True:
        mark = "X" if turn % 2 != 0 else "O"
        print(f"{mark}'s turn")

        row = get_user_input("row")
        column = get_user_input("column")

        if not is_valid_move(row, column):
            print("Invalid move. Try again.")
            continue

        if not is_empty_square(row, column):
            print("This square is already taken. Try again.")
            continue

        update_grid(row, column, mark)
        display_grid()

        winner = check_for_winner()
        if winner in ["X", "O"]:
            print(f"{winner} wins!")
            return True

        if turn == 9:
            print("It's a tie!")
            return True

        turn += 1


# --------------------------------------------------------------------------------------------------------- RECORD INPUT
def get_user_input(coord_type):
    while True:
        try:
            coord = int(input(f"Pick a {coord_type} (1, 2, 3): "))
            if 1 <= coord <= 3:
                return coord
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def is_valid_move(row, column):
    return 1 <= row <= 3 and 1 <= column <= 3


def is_empty_square(row, column):
    return grid[row - 1][column - 1] == " "


def update_grid(row, column, mark):
    grid[row - 1][column - 1] = mark


# --------------------------------------------------------------------------------------------------------- CHECK WINNER
def check_for_winner():
    # Check rows and columns
    for i in range(3):
        if check_line(grid[i][0], grid[i][1], grid[i][2]):  # Check row
            return grid[i][0]
        if check_line(grid[0][i], grid[1][i], grid[2][i]):  # Check column
            return grid[0][i]

    # Check diagonals
    if check_line(grid[0][0], grid[1][1], grid[2][2]):  # Diagonal 1
        return grid[0][0]
    if check_line(grid[0][2], grid[1][1], grid[2][0]):  # Diagonal 2
        return grid[0][2]

    return " "


def check_line(a, b, c):
    return a == b == c and a != " "


# ----------------------------------------------------------------------------------------------------------------------
# if started as the main module, call the main function
if __name__ == "__main__":
    main()
