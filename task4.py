#Write a Python program to split a given list into two parts where the length of the first part of the list is given. Original list: [1, 1, 2, 3, 4, 4, 5, 1] Length of the first part of the list: 3 Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])



def split_list(original_list, split_length):
    # Ensure the split length is within the bounds of the list
    if split_length < 0 or split_length > len(original_list):
        raise ValueError("Split length must be between 0 and the length of the list.")
    
    # Split the list into two parts
    first_part = original_list[:split_length]
    second_part = original_list[split_length:]
    
    return first_part, second_part

# Example usage
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
split_length = 3

first_part, second_part = split_list(original_list, split_length)

print("Original list:")
print(original_list)
print("Length of the first part of the list:", split_length)
print("Splitted the said list into two parts:")
print((first_part, second_part))
