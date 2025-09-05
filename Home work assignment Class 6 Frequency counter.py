"""
BONUS: Word Frequency Counter - Input a string and a specific word, 
output number of instances of that specific word
"""

# Function to count frequency of a specific word in a string
def word_frequency_counter(text, word):
    # Split the text into words and count occurrences of the specified word
    words = text.split()
    count = words.count(word)
    return count

text = input("Enter a string: ")
word = input("Enter the word to count its frequency: ")
frequency = word_frequency_counter(text, word)
print(f"The word '{word}' appears {frequency} times.")  