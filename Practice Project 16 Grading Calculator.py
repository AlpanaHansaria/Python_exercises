"""
16.	Grade Calculator
o	Input marks and calculate grade using functions.
"""

def grade_calculator(marks):
    if marks > 90:
        grade = "A"
    elif marks > 80:
        grade = "B"
    elif marks > 70:
        grade = "C"          
    elif marks > 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def calculate_and_display_grade():
    while True:
        while True:
            students_marks = input("Enter your marks (0-100): ")
            if students_marks.isdigit():
                students_marks = int(students_marks)
                if 0 <= students_marks <= 100:
                    break
                else:
                    print("Invalid input. Please enter marks between 0 and 100.")
            else:
                print("Invalid input. Please enter a number.")

        grade = grade_calculator(students_marks)
        print(f"The grade for marks {students_marks} is: {grade}")

        # Ask if user wants to enter more marks
        again = input("Do you want to enter marks for another student? (y/n): ").lower()
        if again == "n":
            print("Thanks for using the Grade Calculator! Goodbye!")
            break
        elif again != "y":
            print("Invalid input! Exiting the program.")
            break

# Call the function
calculate_and_display_grade()
