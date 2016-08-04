#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
import math
###############################################################################
# Exercise 6.2
# See 6.1: "write a compare function takes two values, x and y, and returns 1
# if x > y, 0 if x == y, and -1 if x < y."
# When you submit only include your final function: compare

def compare(x, y):
    if x > y:
        return 1    #Returns 1 when x is bigger than y
    elif x < y:
        return -1   #Returns -1 when x is less than y
    else:
        return 0    #Returns 0 when x is equal to y

###############################################################################
# Exercise 6.2
# See 6.2: "use incremental development to write a function called hypotenuse
# that returns the length of the hypotenuse of a right triangle given the
# lengths of the other two legs as arguments."
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share in your final push your incremental
# work.

def hypotenuse (x1, x2):
    a = x1**2
    b = x2**2
    c = a + b
    x3 = math.sqrt(c)
    return x3

###############################################################################
# Exercise 6.4
# See 6.4: "write a function is_between(x, y, z) that returns True if x ≤ y ≤ z
# or False otherwise"
# When you submit only include your final function: is_between

def is_between(x, y, z):
    if x <= y <= z:         
        return True         # Returns true if x ≤ y ≤ z
    else:
        return False        # Returns false if x is bigger than y and/or y is bigger than z


###############################################################################
# Exercise 3.2
# See "Exercise 3, part 2": "Write a function called is_palindrome that takes a
# string argument and returns True if it is a palindrome and False otherwise.
# Remember that you can use the built-in function len to check the length of a
# string."
# When you submit only include your final function: is_palindrome

def is_palindrome(s):
    s_length = len(s.strip())       # Calculates length of s without whitespace before or after the word
    if (s_length > 0):              # Checks to see if the string contains at least a letter
        if s[0] == s[-1]:           # Checks if the first letter and the last letter is the same
            new_s = s[1:-2]         # new_s gets rid of first and last letters since they are already checked
            is_palindrome(new_s)    # Runs the function again until there are 2 letters left
            return True             # Returns True if the word is a palindrome
        else:
            return False            # Returns False if the word is not a palindrome
    return False                    # Returns False if the original word does not contain at least a letter


###############################################################################
# Exercise 4
# See "Exercise 4": "A number, a, is a power of b if it is divisible by b and
# a/b is a power of b. Write a function called is_power that takes parameters a
# and b and returns True if a is a power of b. Note: you will have to think
# about the base case."
# Note: Please use the provided definition and only plan for positive integers
# (whole numbers not including zero)
# When you submit only include your final function: is_power

def is_power(a, b):
    if (a % b == 0) and ((a/b) % b == 0):   
        return True                         # Returns true if a is divisible by b and a/b is also divisible by b
    elif a == b:
        return True                         # Returns true if a and b are the same value (base case)
    else:
        return False                        # Returne false if a and a/b are not divisible by b and a does not equal b




###############################################################################
def main():
    """Your functions will be called within this function."""
    ###########################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")


    ###########################################################################
    # # Uncomment the below to test and before commiting:
    # # Exercise 1
    print(compare(1, 1))
    print(compare(1, 2))
    print(compare(2, 1))
    # # # Exercise 2
    print(hypotenuse(1, 1))
    print(hypotenuse(3, 4))
    print(hypotenuse(1.2, 12))
    # # # Exercise 3
    print(is_between(1, 2, 3))
    print(is_between(2, 1, 3))
    print(is_between(3, 1, 2))
    print(is_between(1, 1, 2))
    # # # Exercise 6
    print(is_palindrome("Python"))
    print(is_palindrome("evitative"))
    print(is_palindrome("sememes"))
    print(is_palindrome("oooooooooooo"))
    # # # Exercise 7
    print(is_power(28, 3))
    print(is_power(27, 3))
    print(is_power(248832, 12))
    print(is_power(248844, 12))


if __name__ == "__main__":
    main()
