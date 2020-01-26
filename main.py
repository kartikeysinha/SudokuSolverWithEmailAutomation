import yagmail # For automation of email sending

print("Please input a number between 1 to 9")
print("If there is no number in the space, input 0.")
print("Make sure that there is no spaces between the numbers.")

# Ask for the input for 9 rows of the sudoku puzzle.

EMAIL = input("PLease enter your E-Mail to get solution sent: ")
str1 = input("Please input row 1: ")
str2 = input("Please input row 2: ")
str3 = input("Please input row 3: ")
str4 = input("Please input row 4: ")
str5 = input("Please input row 5: ")
str6 = input("Please input row 6: ")
str7 = input("Please input row 7: ")
str8 = input("Please input row 8: ")
str9 = input("Please input row 9: ")


# Define the initial Sudoku-Grid in the form of list of strings.
sudoku = ([str1, str2, str3, str4, str5,
           str6, str7, str8, str9])

# Function to convert a string to a list of characters.
def string_to_list(ss):
    return [char for char in ss]

# Recursion to covert the list of strings to form a Sudoku-Grid.
def build_sudoku(lol):
    if len(lol) == 1:
        return [string_to_list(lol[0])]
    else:
        return [string_to_list(lol[1])] + build_sudoku(lol[1:])


board = build_sudoku(sudoku)

# Finds an empty spot on the board.
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

# Solves the board by inputting valid numbers.
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

# checks if the the inputted number is valid.
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

# prints the solved board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


### -- email testing start -- ##

sender_email = 'sudokusoln@gmail.com' # dummy email
sender_password = 'BforBall!'         # dummy email's password

receiver_email = '{}'.format(EMAIL)

yag = yagmail.SMTP(user=sender_email, password=sender_password)

subject = 'Sudoku Solution is Here'
contents = ['{}'.format(build_sudoku(sudoku))] # contents should be replace with
                                               # string_display -> solve -> build sudoku -> sudoku

yag.send(to=receiver_email,subject=subject,contents=contents)

### -- email testing end -- ###

print("The solution has been succesfully sent to the given E-Mail.")




