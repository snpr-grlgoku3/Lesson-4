# Taking input from the user
number = float(input("Enter a number: "))

# Checking if the number is non-negative
if number < 0:
    print("Error: Cannot calculate the square root of a negative number.")
else:
    # Calculating the square root
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}.")