# Python program to find the root of a given function using Binary Search
import math
import numpy as np

# Define a continuous function 'f' where f(x) = x^4 - x^2 - 10
def f(x):
    return x**4 - x**2 - 10

# Define the binary search function 
def binary_search(func, target, left, right, precision):
    while (right - left) > precision:
        middle = (left + right) / 2
        if np.abs(func(middle) - target) < precision:
            return middle
        elif func(middle) < target:
            left = middle
        else: 
            right = middle 
    return (left + right) / 2

epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 50  # target value for root of function 'f'
start = -5  # starting point of the interval
end = 5  # ending point of the interval

result = binary_search(f, target, start, end, epsilon)
print(f"The value of x for which f(x) is approximately {target} within the interval [{start}, {end}] is: {result:.6f}")