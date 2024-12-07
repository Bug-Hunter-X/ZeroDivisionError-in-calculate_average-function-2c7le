def calculate_average(numbers):
    total = sum(numbers)
    if len(numbers) == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    average = total / len(numbers)
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")