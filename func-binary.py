import numpy as np

# Define a continuous function 'f' where f(x) = x^6 - 3x^4 + 4x^3 - 1
def f(x):
    return x**6 - 3 * x**4 + 4 * x**3 - 1

# Binary Search Function for finding where f(x) = target
def binary_search(func, target, left, right, epsilon):
    while (right - left) > epsilon:
        middle = (left + right) / 2
        if np.abs(func(middle) - target) < epsilon:  # If close enough to target
            return middle
        elif func(left) * func(middle) < 0:  # Root is in the left half
            right = middle
        else:  # Root is in the right half
            left = middle
    return (left + right) / 2

epsilon = 1e-6  # Precision tolerance
target = 0  # We want to find where f(x) = 0
start = -5  # Start of the search interval
end = 5  # End of the search interval

result = binary_search(f, target, start, end, epsilon)
print(f"The value of x for which f(x) is approximately {target} is: {result:.6f}")
