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





