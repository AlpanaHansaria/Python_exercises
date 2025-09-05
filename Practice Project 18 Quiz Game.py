"""
18.	Quiz Game
o	Store questions and answers in a file or dictionary.
o	Ask questions randomly and calculate score.
"""

# Large dictionary of questions and answers
import random

qa_dict = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the largest planet in our Solar System?": "Jupiter",
    "What is the boiling point of water in Celsius?": "100 Degree C",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the smallest prime number?": "2",
    "What is the chemical symbol for gold?": "Au",
    "How many continents are there on Earth?": "7",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the fastest land animal?": "Cheetah",
    "Who discovered penicillin?": "Alexander Fleming",
    "What is the tallest mountain in the world?": "Mount Everest",
    "In which year did the Titanic sink?": "1912",
    "Who is known as the father of computers?": "Charles Babbage",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Which gas do plants absorb from the atmosphere?": "Carbon Dioxide",
    "Who was the first person to walk on the moon?": "Neil Armstrong",
    "What is the hardest natural substance on Earth?": "Diamond",
    "Which element has the atomic number 1?": "Hydrogen",
    "What is the main language spoken in Brazil?": "Portuguese",
    "Who wrote '1984'?": "George Orwell",
    "What is the currency of Japan?": "Yen",
    "Which organ in the human body produces insulin?": "Pancreas",
    "What is the smallest country in the world?": "Vatican City",
    "Which planet has the most moons?": "Saturn"
}

# Number of questions you want in the quiz
num_questions = 10

# Select a random subset of questions
random_questions = random.sample(list(qa_dict.items()), num_questions)

# Initialize score
score = 0

# Loop through each question
for question, correct_answer in random_questions:
    print("\n" + question)
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == correct_answer.lower():
        print("Correct! +10 points")
        score += 10
    else:
        print(f"Incorrect! The correct answer is: {correct_answer} (0 points)")

# Print total score
print("\nQuiz Completed!")
print(f"Your total score is: {score} out of {num_questions * 10}")