import os

def get_terminal_size():
    try:
        columns, rows = os.get_terminal_size()
    except OSError:
        columns, rows = 80, 24  # Default size
    return columns, rows

def main():
    columns, rows = get_terminal_size()

    # Print column numbers
    for i in range(columns):
        print(f"{i % 10}", end="")
    print()

    # Print grid
    for row in range(rows - 2):  # -2 to leave space for the bottom row and prompt
        if row < 26:
            print(chr(ord('a') + row))
        else:
            print(" ")

    # Print bottom row
    for i in range(columns):
        print(f"{i % 10}", end="")
    print()


if __name__ == "__main__":
    main()
