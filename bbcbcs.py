size = int(input("Enter an odd size (3 or more): "))
if size < 3 or size % 2 == 0:
    print("Please enter an odd number of at least 3.")
else:
    middle = size // 2
    # Top half, including the middle row
    for row in range(middle + 1):
        spaces = middle - row
        inside = 2 * row - 
        if row == 0:
            print(" " * spaces + "*")
        else:
            print(" " * spaces + "*" + " " * inside + "*")

    # Bottom half
    for row in range(middle - 1, -1, -1):
        spaces = middle - row
        inside = 2 * row - 1

        if row == 0:
            print(" " * spaces + "*")
        else:
            print(" " * spaces + "*" + " " * inside + "*")

