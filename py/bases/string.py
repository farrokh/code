# string is a class that contains methods for string manipulation
# string is immutable
# string is a sequence of characters
# string is a sequence of bytes

# escaping characters
# \n new line
# \t tab
# \r carriage return
# \f form feed
# \b backspace
# \a bell
# \v vertical tab

# multiline string
# """
# """

# putting \ in a string will escape the character. example:
print("I am 6'2\" tall.") # this will print I am 6'2" tall.
print('It\'s a string') # this will print It's a string

# we cant change a character in a string. example:
name = "John"
name[0] = "J"
print(name) # this will print an error

# substring
# example:
name = "John"
print(name[0:2]) # this will print Jo
#  the first number is the starting index, the second number is the ending index. end is not included. there also an option to specify the step. example:
print(name[0:2:1]) # this will print Jo
#  the step is the number of characters to skip. example:
print(name[0:2:2]) # this will print J
#  the step is negative. example:
print(name[0:2:-1]) # this will print J
#  the step is zero. example:
print(name[0:2:0]) # this will print an error
# reverse a string using slicing
# example:
name = "John"
print(name[::-1]) # this will print nhoJ


# concatenate strings
# example:
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name) # this will print John Smith

# or
full_name = " ".join([first_name, last_name]) # !!! this is very useful when we want to join a list of strings
# another example:
my_list = ["a"]*5
print(my_list) # this will print ['a', 'a', 'a', 'a', 'a']
my_string = "".join(my_list)
print(my_string) # this will print aaaaa

# check if a character is in a string
# example:
name = "John"
print("J" in name) # this will print True
#  we can check substrings as well
print("oh" in name) # this will print True


# remove whitespace
name = " John      "
print(name) # this will print John
print(name.strip()) # this will print John
# !!! strings are immutable. we cant change a string. so we need to create a new string.

## string methods
# upper()
# lower()
# title()
# count()   # count the number of times a substring occurs in a string
# find() # returns the index of the first occurrence of the substring
# index() # returns the index of the first occurrence of the substring

# replace() example:
name = "John"
print(name.replace("J", "j")) # this will print john
# !!! strings are immutable. we cant change a string. so we need to create a new string.

# split()
# join()
# strip()
# lstrip()  # removes whitespace from the left side of the string
# rstrip()  # removes whitespace from the right side of the string
# isalpha() # checks if all characters in the string are alphabetic
# isdigit() # checks if all characters in the string are digits
# isalnum() # checks if all characters in the string are alphanumeric. this is the combination of isalpha() and isdigit()

# convert sentence to list
# example:
sentence = "I am 6'2\" tall."
words = sentence.split() 
print(words) # this will print ['I', 'am', '6\'2"', 'tall.']
# by default, this will split the string into words. we can also specify the separator. example:
sentence = "I am 6'2\" tall."
words = sentence.split("a")
print(words) # this will print ['I ', 'm 6\'2" t','ll.']


## format strings
# % example:
name = "John"
age = 23
print("His name is %s and he is %d years old." % (name, age)) # this will print His name is John and he is 23 years old.

# format example:
name = "John"
age = 23
print("His name is {0} and he is {1} years old.".format(name, age)) # this will print His name is John and he is 23 years old.

# fstring (python 3.6+)
# example:
name = "John"
age = 23
print(f"His name is {name} and he is {age} years old.") # this will print His name is John and he is 23 years old.
