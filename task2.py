#Write a Python program to get the largest and smallest number from a list without builtin functions

def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None  # Return None if the list is empty

    # Initialize largest and smallest with the first element
    largest = smallest = numbers[0]

    # Iterate through the list
    for num in numbers:
        if num > largest:
            largest = num  # Update largest if current number is greater
        if num < smallest:
            smallest = num  # Update smallest if current number is smaller

    return largest, smallest

# Example usage
numbers_list = [34, 1, 78, 12, -5, 0, 99]
largest, smallest = find_largest_and_smallest(numbers_list)
print("Largest number:", largest)
print("Smallest number:", smallest)
