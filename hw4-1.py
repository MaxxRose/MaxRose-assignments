#Write a separate program to accomplish each of these exercises. Save each program 
# with a filename that follows standard Python conventions, using lowercase 
# letters and underscores, such as simple_message.py and simple_messages.py.

# EXERCISE 1: Simple Messages
# Assign a message to a variable, and print that message. 
# Then change the value of the variable to a new message, and print the new message.
message = "My name is Jinu" #Here, I'm assigning the string "My name is Jinu" to the variable 'message'.
print(message)
message = "My name is Max"
print(message)

# EXERCISE 2: Personal Message
# Use a variable to represent a person’s name, and print a message to that person. 
# Your message should be simple, such as, “Hello Umika, would you like to learn some
# Python today?”
name = "Dave"
message2 = "How are you doing today?"
print(name+", "+ message2) 
name = "Stevo"
message2 = "How are you still alive?"
print(name+", "+ message2) 


# EXERCISE 3a: Quotes
# Find a quote from a famous person. Print the quote and the name of its author. 
# Your output should look something like the following, including the quotation marks: 
# Albert Einstein once said, “A person who never made a mistake never tried anything
# new.”
print('Rene Descartes once said, "I think, therefore I am"')
print('Sir Neil Degrasse Tyson once said, "something about science"')
# EXERCISE 3b: Quotes
# Repeat Exercise 3a, but this time, represent the famous person’s name using a 
# variable called famous_person. Then compose your message and represent it with a 
# new variable called message. Print your message.
famous_person = "Rene Descartes"
message3 = '"I think, therefore I am"'
print(famous_person+" once said,", message3)
famous_person = "Sir Neil Degrasse Tyson" #this quote makes me cry everytime
message3 = '"something about science"'
print(famous_person+" once said,", message3)

# EXERCISE 4: Number Eight
# Write addition, subtraction, multiplication, and division operations that each 
# result in the number 8. Be sure to enclose your operations in print() calls to see
# the results. You should create four lines that look like this: print(5+3) 
# Your output should simply be four lines with the number 8 appearing once on each line.
print(2+6) #Here, in the print function, there is the '+' operator, which represents addition. In this line of code, 2 is being added onto 6, which makes 8.
print(2*4)
print(10-2)
print(16/2)
print(5+3) #My code starts here
print(8*1)
print(11-3)
print(24/4)

# EXERCISE 5:  Adding Comments
# Choose two of the programs you’ve written, and add at least one comment to each.
#  If you don’t have anything specific to write b, just add your name and the current
# date at the top of each program file. Then write one sentence describing what the 
# program does.
#added comments to lines 39 & 52

# EXERCISE 6: Rental Car
# Write a program that asks the user what kind of rental car they would like. Print
#  a message about that car, such as “Let me see if I can find you a Subaru.”
user_input=input("What kind of car would you like?")
print("Let me find you that brand's best model!")
user_input=input("Do would like car?")
print("yes!")

# EXERCISE 7: Restaurant Seating
# Write a program that asks the user how many people are in their dinner group. If 
# the answer is more than eight, print a message saying they’ll have to wait for a
# table. Otherwise, report that their table is ready.
# Hint: use an if statement
user_input2=int(input("How many people are in your group?"))
if(user_input2>=8):
    print("You'll have to wait for a table")
else:
    print("Your table is ready!")

user_input2=int(input("How many group people?"))
if(user_input2>=43.5):
    print("no table")
else:
    print("table!")


# EXERCISE 8: Multiples of Ten
# Ask the user for a number, and then report whether the number is a multiple of 10
# or not.
# Hint: use the modulo operator % to get the remainder after division by 10
user_input3=int(input("Pick any number! "))
number = user_input3
if number%10==0:
    print(str(number)+" is a multiple of 10.")
else:
    print(str(number)+" is not a multiple of 10.")   

user_input3=int(input("!Pick number! "))
number = user_input3
if number%10==0:
    print(str(number)+" It 10.")
else:
    print(str(number)+"not 10.")   

# EXERCISE 9a: T-Shirt 
# Write a function called make_shirt() that accepts a size and the text of a message
# that should be printed on the shirt. The function should print a sentence 
# summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.
def make_shirt(size, msg):
    print("This shirt is size "+size+", and the message on it is "+msg)
make_shirt("XL","I like pancakes!")
make_shirt(size="XL", msg="I like pancakes!")

def make_shirt(size, msg):
    print(" shirt size "+size+", and message is "+msg)
make_shirt("XXL","Like pancakes!")
make_shirt(size="XXL", msg="like pancakes!")

# EXERCISE 9b: T-Shirt
# Modify the make_shirt() function so that shirts are large by default with a message
# that reads “I love Python”. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any
# size with a different message.
def make_shirt2(size="large", msg="I love Python and it loves me"):
    print("This shirt is size "+size+", and the message on it is "+msg)
make_shirt2()
make_shirt2(size="large")
make_shirt2(size="large", msg="I want to write some code")

def make_shirt3(size="small", msg="I love grass"):
    print("shirt size "+size+", and the message on it is "+msg)
make_shirt3()
make_shirt3(size="Medium")
make_shirt3(size="Medium", msg="gee I love touching grass")

# EXERCISE 9b: T-Shirt
# Modify the make_shirt() function so that shirts are large by default with a message
# that reads “I love Python”. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any
# size with a different message.
def make_shirt4(size="large", msg="I love Python"):
    print("This shirt is size "+size+", and the message on it is "+msg)
make_shirt4()
make_shirt4(size="large")
make_shirt4(size="large", msg="I want to write some code")

def make_shirt5(size="medium", msg="I love cheese"):
    print("This shirt is size "+size+", and the message on it is "+msg)
make_shirt5()
make_shirt5(size="medium")
make_shirt5(size="medium", msg="I want the DPRK")

def make_shirt6(size="small", msg="I love grass"):
    print("shirt size "+size+", and the message on it is "+msg)
make_shirt6()
make_shirt6(size="small")
make_shirt6(size="small", msg="gee I love touching grass")