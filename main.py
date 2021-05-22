'''
--------------------------------------
| Student  :  Mihir Kachroo          |
| Teacher  :  Mr. Ghorvei            |
| Date     :  May 14th 2021          |
| Program  :  Calculator             |
--------------------------------------
Features of this app
  Solves one step math expressions in word or math format
  Basic natural language processing
  Supports addition, subtraction, multiplication, division, exponents, radicals, logarithms, modulus, floor division, greatest common factor, and least common multiple
  Allows user to display calculator history
  Allows user to clear console

Limitations
  Symbols and numbers have to be seperated by a space
  One step expressions only
'''
# imports all the mathematical functions individually from my mathFunctions.py file
# Allows me to call these functions later on in my code
from mathFunctions import add, subtract, multiply, divide, exponent, radical, modulus, floorDivision, log, greatestCommonFactor, leastCommonMultiple
import os # Imports the os module which I use to control the command line

# Prints introduction header
print("{0}  Welcome to Mihir's calculator {0}\n".format('-'*15)) # The -*10 prints the "-" 10 times to create a dashed header line
name = input("Please enter your name: ") # Asks user to input that name and stores it as a string in variable name
print("\nHi {}, here is how you use the app: ".format(name))
# Prints instructions for using app
print(" Enter a expression with 2 numbers and 1 operator (word or symbol) \n Seperate the numbers and operators with spaces \n Supported operations are +, -, *, /, **, root, %, //, log, gcf and lcm\n Supported user commands are history, clear, and exit\n")
# Prints examples of possible operations that the user can input
print("Examples of expressions you can type:\n 17 * 2\n 13 // 4\n please add 16 with -12\n what is the 2 root of 4\n Find the gcf of 9 and 12\n")
# List that stores and is used to display past inputed calculator expressions
calculatorHistory = []
# Variable that tracks if the user has chosen to exit the code yet. Is used to continue or break the while loop
didUserExit = False

# Returns list of all the numbers in the expression
def extractNumbersFromString(text):
  listOfNumbers=[] # Stores the numbers from the expression
  # Splits by entered expression by spaces and loops over each block
  for t in text.split(' '):
    try: # Tries to add value to list
      # If value is a number (float), adds it to list of numbers
      listOfNumbers.append(float(t))
    # If value is not a float number, throws value error exception, does not add value to list and continues loop
    except ValueError:
      pass # Does nothing to avoid error and allow loop to continue
  return listOfNumbers

# Displays past calculator operations
def displayCalculatorHistory():
  print("Here is your calculator history:")
  # Only displays history if more than one operations have been performed in the past
  if len(calculatorHistory) >= 0:
    # Loops over calculator history list and prints every expression
    for expression in calculatorHistory:
      print("   {}".format(expression))
  # Prints calculator history is empty if there are no past operations performed
  else:
    print("Calculator history is empty")
  print('\n')

# Clears the console to make command line easier to read for user
def clearConsole():
  os.system('clear') # Uses os module to clear command prompt

# Prints ending statement and exists program
def end():
  print("Thank you for using Mihir's Calculator {}!".format(name))
  # Acceses the didUserExit variable in the global scope instead of creating a new local didUserExist variable
  global didUserExit
  didUserExit = True # Sets the global didUserExit value to True so that the while loop breaks

# Dictionary of user commands  that map key words to functions
# exit, end, leave and close all point to the end function so that the user can type in any one of these values to exit the program
commands={'history':displayCalculatorHistory, 'clear':clearConsole, 'exit':end, 'end':end, 'leave':end, 'close':end}

# Dictionary of operations that map key words to functions
# Multiple words and symbols can map to the same function allowing the user to use any one of those keys to call a function
operations={'+':add, 'add':add,'sum':add,'plus':add,'addition':add,
  '-':subtract, 'subtraction':subtract,'subtract':subtract, 'minus':subtract,'difference':subtract, '*': multiply,
  'product':multiply, 'multiply':multiply,'multiplication':multiply, '/':divide,'division':divide, '**': exponent, 'exponent': exponent, 'power': exponent, 'root': radical, '%': modulus, 'modulus': modulus, 'remainder': modulus, '//': floorDivision, 'floor': floorDivision, 'log':log, 'logarithm':log, 'gcf':greatestCommonFactor, 'gcd':greatestCommonFactor, 'lcm': leastCommonMultiple}

# Infinitely runs the block of code below as long as didUserExit is not true. If it becomes False, it stops looping
while didUserExit == False:
  # Stores the users inputed expression as a string. New input is asked for everytime the while loop reruns the block
  expression = input('Enter your expression: ')
  # Variable to track if there is a expression or command in the entered expression
  isThereOperationOrCommand = False
  # Splits the entered expression by spaces and loops over every word
  for word in expression.split(' '):
    # Puts word in lower case and checks if it is a key in operations dictionary
    if word.lower() in operations.keys():
      # Tries the following code
      try:
        # Maps the returned 2 value list from extractNumbersFromString function to numOne and numTwo
        numOne, numTwo = extractNumbersFromString(expression)
        # Searches operations dictionary by the word key in lower case and executes its relating function. By putting the word in lowercase like the keys in the operations dict, we avoid capitalization differences
        result = operations[word.lower()] (numOne,numTwo)
        calculatorHistory.append(result) # Adds the result to calculator history list
        print("  {} \n".format(result)) # Prints gotten result
      # If there is an error with the recieved list from extractNumbersFromString because less than two values were returned, tells the user to try again and include two numbers in the expression
      except:
        print(" Error! Please make sure your expression has exactly two numbers that are split by spaces")
      # Runs this if there is or isn't an exception
      finally:
        isThereOperationOrCommand = True # Sets variable to True because there was a operation found in the sentence
        break # Terminates while loop
    # Puts word in lower case and checks if it is a key in user commands dictionary. By putting it in lowercase like the keys in the user commands dict, we avoid capitalization differences
    elif word.lower() in commands.keys():
      # Searches commands dictionary by the word key and executes its relating function
      commands[word.lower()]()
      isThereOperationOrCommand = True # Sets variable to True because there was a user command found in the sentence
      break # Terminates while loop
  # Executes if there is no operation or command key in expression
  if not isThereOperationOrCommand:
    print(" Error! Please enter a valid expression split by spaces with one of the defined operations or user commands \n")