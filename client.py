print "Welcome to Python!"



my_variable = 10

print my_variable



my_int = 7
my_float = 1.23
my_bool = True

print my_int
print my_float
print my_bool


my_int = 7

my_int = 3



# variable assignment
mysterious_variable = 42



"""Sipping from your cup 'til it runneth over,
Holy Grail.
"""

# Sipping from your cup 'til it runneth over,
# Holy Grail.



# math
addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9

count_to = 5000 + 6000
print count_to


# exponentiation
eggs = 10 ** 2
print eggs


# modulo
spam = 8 % 7
print spam


# access by index
+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5
fifth_letter = "PYTHON"[4]

print fifth_letter


# string methods
len()
lower()
upper()
str()

parrot = "Norwegian Blue"
print len(parrot)

# lower method
"Ryan".lower()  # returns "ryan"

# upper method
"ryan".upper()  # returns "RYAN"

# str method
pi = 3.14
print str(pi)

# dot notation
# methods that use dot notation only work with strings
# len() and str() can work on other data types
ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()


# concatenation
print "Life " + "of " + "Brian"


# explicit string conversion
print "I have " + str(2) + " coconuts!"


# The % operator after the string is used to combine a string with variables
name = "Winnie"
print "Hello %s" % (name)


# If you’d like to print a variable that is an integer, you can “pad” it with
# zeros using %02d. The 0 means “pad with zeros”, the 2 means to pad to 2
# characters wide, and the d means the number is a signed integer
# (can be positive or negative).
day = 6
print "03 - %s - 2021" %  (day)
# 03 - 6 - 2021
print "03 - %02d - 2021" % (day)
# 03 - 06 - 2021
