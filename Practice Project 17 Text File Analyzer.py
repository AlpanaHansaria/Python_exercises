"""
17.	Text File Analyzer
o	Count lines, words, and characters in a text file.
"""

import os

# Take folder path and file name from user
FILE_PATH = input("Enter the full path of the folder containing the file: ")
FILE_NAME = input("Enter the file name (e.g., tasks.txt): ")

# Combine path and file name
FULL_PATH = os.path.join(FILE_PATH, FILE_NAME)

# Initialize counters
line_count = 0
word_count = 0
char_count = 0

try:
    # Open and read the file
    with open(FULL_PATH, "r") as f:
        for line in f:
            line_count += 1                 # Count lines
            words = line.split()            # Split line into words
            word_count += len(words)        # Count words
            char_count += len(line)         # Count characters including spaces and newline

    # Print results
    print(f"{FILE_NAME} has {line_count} Lines.")
    print(f"{FILE_NAME} has {word_count} Words.")
    print(f"{FILE_NAME} has {char_count} Characters.")

except FileNotFoundError:
    print(f"Error: The file '{FULL_PATH}' does not exist. Please check the path and try again.")