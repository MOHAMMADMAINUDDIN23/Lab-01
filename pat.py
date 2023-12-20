def print_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

num_rows = int(input("Enter no of rows:"))
print_pyramid(num_rows)


