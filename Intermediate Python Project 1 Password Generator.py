"""
A. Intermediate Python Projects
Focus: OOP, algorithms, file handling, web scraping, APIs
1.	Password Generator
o	Generate strong passwords with letters, digits, symbols.
o	Bonus: Save passwords securely to a file.
"""

import random
import string
import os

# Set the directory where you want to save the password file
new_directory = "C:\\Users\\Alpan\\OneDrive\\Documents\\GitHub\\Python_exercises\\Files_created_by_python_scripts"
os.chdir(new_directory)

# Create a list containing letters, numbers, and special characters
characters = list(string.ascii_letters + string.digits + string.punctuation)

# Randomly select 8 characters
random_selection = ''.join(random.choices(characters, k=8))

# Define the filename
file_name = "passwords.txt"

# Write the password to the text file
with open(file_name, "w") as file:
    file.write(random_selection)

print(f"Password '{random_selection}' has been written to {file_name}")