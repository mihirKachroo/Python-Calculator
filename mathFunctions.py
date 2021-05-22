# Module that allows me to use mathematical functions defined by the C standard
import math
'''
This is the file where I have written my functions for adding, subtracting, multiplying, dividing, exponents, radicals, logarithms, modulus, floor division, and finding the greatest common factor and least common multiple.

I import all the functions from this file in main.py
'''

# Function to add two numbers
def add(firstNumber, secondNumber):
  return "{} + {} = {}".format(firstNumber, secondNumber, float(firstNumber+secondNumber)) # Returns equation string and formats answer to float

# Function to subtract two numbers
def subtract(firstNumber, secondNumber):
  return "{} - {} = {}".format(firstNumber, secondNumber, float(firstNumber-secondNumber)) # Returns equation string and formats answer to float

# Function to multiply two numbers
def multiply(firstNumber, secondNumber):
  return "{} * {} = {}".format(firstNumber, secondNumber, float(firstNumber*secondNumber)) # Returns equation string and formats answer to float

# Function to divide two numbers
def divide(firstNumber, secondNumber):
  return "{} / {} = {}".format(firstNumber, secondNumber, float(firstNumber/secondNumber)) # Returns equation string and formats answer to float

# Function to get exponent
def exponent(base, power):
  return "{} ** {} = {}".format(base, power, float(base**power)) # Returns equation string and formats answer to float

# Function to solve radical expression
def radical(root, number):
  return "{}√{} = {}".format(int(root), number, float(number ** (1/root))) # Returns equation string and formats answer to float

# Function to find logarithmic bases using math module
def log(base, a):
  return "Logarithm base {} of {} = {}".format(base, a, float(math.log(a, base))) # Returns equation string and formats answer to float

# Function to get remainder between two operands
def modulus(firstNumber, secondNumber):
  return "{} % {} = {}".format(firstNumber, secondNumber, float(firstNumber%secondNumber)) # Returns equation string and formats answer to float

# Function to divide two numbers and return the largest possible integer
def floorDivision(firstNumber, secondNumber):
  return "{} // {} = {}".format(firstNumber, secondNumber, int(firstNumber//secondNumber)) # Returns equation string and formats answer to int

# Function to get the greatest common factor between two numbers
def greatestCommonFactor(firstNumber, secondNumber):
  initialFirstNumber, initialSecondNumber = firstNumber, secondNumber # Remembers the firstNumber and secondNumber sent through parameters before they are changed in while loop
  # Loops till secondNumber is not equal to 0 which is when the gcf has been found
  while secondNumber != 0:
    # Sets firstNumber to secondNumber and secondNumber to remainder of firstNumber divided by secondNumber
    (firstNumber, secondNumber) = (secondNumber, firstNumber % secondNumber)
  return "Greatest common factor of {} and {} = {}".format(initialFirstNumber, initialSecondNumber, firstNumber) # Returns equation string

# Function to find the least common multiple between two numbers
def leastCommonMultiple(firstNumber, secondNumber):
  # choose the bigger number using a shorthand if/else statement
  greater = firstNumber if firstNumber > secondNumber else secondNumber
  # Creates an forever running loop
  while True:
    # Checks if both first number and second number are perfectly divisible by the greater variable
    if((greater % firstNumber == 0) and (greater % secondNumber == 0)):
      lcm = greater # Sets lcm to the greater multiple
      break # Terminates the while loop
    greater += 1 # Shorthand that increases the greater variable by one
  return "Least common multiple of {} and {} = {}".format(firstNumber, secondNumber, float(lcm)) # Returns equation string and formats answer to float