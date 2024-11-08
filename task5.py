#Write a Python program to traverse a given list in reverse order, and print the elements with the original index. Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order: black white green red


# Original list
original_list = ['red', 'green', 'white', 'black']

# Traverse the list in reverse order
print("Traverse the said list in reverse order:")
for index in range(len(original_list) - 1, -1, -1):
    print(f"{original_list[index]} (original index: {index})")
