#Now, imagine blasting off from 2 and 3 instead, isn't that galactic? In this task, I want you to construct a function that takes an integer n and parachutes back with the n-th number in our ship-shaped Fibonacci sequence. 
def alt_fib(n):
    if n == 0:
        return 2
    elif n == 1:
        return 3
    else:
        return alt_fib(n -1) +alt_fib(n - 2 )
    # Test the function with some values
print(alt_fib(0))  # Expected output: 2
print(alt_fib(1))  # Expected output: 3
print(alt_fib(2))  # Expected output: 5
print(alt_fib(3))  # Expected output: 8
print(alt_fib(4))  # Expected output: 13
print(alt_fib(5))  # Expected output: 21