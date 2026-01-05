"""This program takes a user's first name and last name as input.
Concatenates the first name and last name into a full name.
Prints a personalized greeting message using the full name."""
#Taking input of name from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
#Capitilising the first letter and lowercase the remaining letter of first and the last name
first_name = first_name.title()
last_name = last_name.title()
#Concatenating the first name and last name into a full name.
full_name = first_name + ' ' + last_name
#printing the Personalised Greeting Message
print("Hello, " + full_name + "! " + "Welcome to the Python Program.")