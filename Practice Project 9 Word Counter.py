"""
9.	Word Counter
o	Input a sentence and count number of words.
o	Bonus: Count frequency of each word.
"""

def word_counter():
    while True:
        user_input = input("Enter a sentence (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the Word Counter. Goodbye!")
            break

        # Count words
        words = user_input.split()
        print(f"Number of words: {len(words)}")

        # Count frequency of each word
        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        print("Word frequency:")
        for word, count in word_frequency.items():
            print(f"'{word}': {count}")

# Run the Word Counter
word_counter()