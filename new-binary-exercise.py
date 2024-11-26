# Implementation of Binary Search on a specific use case

# List of sorted ages in a social media platform
ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1  # Correct bounds: highest valid index

    while low <= high:  # Corrected condition
        mid = (low + high) // 2
        if target == data[mid]:  # If target is found
            return mid
        elif target < data[mid]:  # Search in the left half
            high = mid - 1
        else:  # Search in the right half
            low = mid + 1
    
    return None  # Return None if the target is not found

# Query for age 30
age_query = 30
result = binary_search_iterative(ages, age_query)

if result is not None:
    print(f"Age {age_query} is found at position {result} in the age list.")
else:
    print(f"No profile is found with age {age_query}.")