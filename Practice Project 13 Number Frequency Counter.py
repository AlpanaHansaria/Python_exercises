"""
13.	Number Frequency Counter
o	Count how many times each number occurs in a list.
"""

def freq_count():
    my_list = list(map(int, input("Enter numbers separated by space: ").split()))
    frequency = {}
    for num in my_list:
        frequency[num] = frequency.get(num, 0) + 1

    print("Number Frequency:")
    for num, count in frequency.items():
        print(f"Number {num}: {count} time(s)")

#Run the function
freq_count()