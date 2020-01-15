print("Please input a number between 1 to 9")
print("If there is no number in the space, input 0.")
print("Make sure that there is no spaces between the numbers.")

# Ask for the input for 9 rows of the sudoku puzzle.

str1 = input("Please input row 1:")
str2 = input("Please input row 2:")
str3 = input("Please input row 3:")
str4 = input("Please input row 4:")
str5 = input("Please input row 5:")
str6 = input("Please input row 6:")
str7 = input("Please input row 7:")
str8 = input("Please input row 8:")
str9 = input("Please input row 9:")


# define the initial sudoku grid in the form of list of strings.
sudoku = ([str1, str2, str3, str4, str5,
           str6, str7, str8, str9])

# Function to convert a strinng to a list of characters.
def string_to_list(ss):
    return [char for char in ss]

# Recursion to covert the list of strings to form a sudoku grid.
def build_sudoku(lol):
    if len(lol) == 1:
        return [string_to_list(lol[0])]
    else:
        return [string_to_list(lol[1])] + build_sudoku(lol[1:])






