#Write a Python program to find duplicate values from a list and display those.

def find_duplicates ```python
def find_duplicates(input_list):
    unique_list = []
    duplicate_list = []
    
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
        elif item not in duplicate_list:
            duplicate_list.append(item)
    
    return duplicate_list

# Example usage
input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
duplicates = find_duplicates(input_list)
print("Duplicate values:", duplicates)
