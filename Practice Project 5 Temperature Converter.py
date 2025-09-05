""""
5.	Temperature Converter
o	Convert Celsius ↔ Fahrenheit.
o	Bonus: Convert Kelvin as well.
"""

def c_to_f(c):
    return (c * 9/5) + 32

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

def temp_conv():
    while True:
        temp = input("Enter temperature (e.g., 36C, 100F, 300K) or 'exit': ")
        if temp.lower() == 'exit':
            print("Exiting the Temperature Converter. Goodbye!")
            break

        try:
            value = float(temp[:-1])
            unit = temp[-1].upper()

            if unit == 'C':
                fahrenheit = c_to_f(value)
                print(f"{value}°C is {fahrenheit:.2f}°F")
            elif unit == 'K':
                fahrenheit = k_to_f(value)
                print(f"{value}K is {fahrenheit:.2f}°F")
            else:
                print("Invalid unit! Please use C for Celsius, or K for Kelvin.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid temperature like 36C, 100F, or 300K.")

        # Ask user if they want to continue
        while True:
            cont = input("\nDo you want to convert another temperature? (y/n): ").lower()
            if cont == 'y':
                break  # Continue outer loop
            elif cont == 'n':
                print("Thanks for using the Temperature Converter! Goodbye!")
                return  # Exit the function completely
            else:
                print("Invalid input! Please enter 'y' for yes or 'n' for no.")

# Run the Temperature Converter
temp_conv()
