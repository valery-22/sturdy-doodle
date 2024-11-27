# TODO: Given a sorted list of grades in a class, implement Binary Search on this list
grades = [35, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

def binary_search(grades, target):
    left, right = 0, len(grades) - 1
    
    while left <= right:
        mid = (left + right) //2
        if grades[mid] == target:
            return mid
        elif grades[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1
# TODO: Implement the Loop-based Binary Search function without recursion
grades = [i for i in range(35,95)]
# TODO: Set a query for a student's grade for your search
grades_query = 50

# TODO: Invoke the Binary Search function. If you find the grade, print the position in the grade list; if not, print a not found message.

    
result = binary_search(grades,grades_query)

if result != -1:
    print(f"Grade{grades_query} found at position {result}")
else:
    print(f"Grade {grades_query} not found.")