def recursiveSumEven(arr, idx=0):
    # implement this
    if idx >= len(arr):
        return 0
    
    return arr[idx] + recursiveSumEven(arr, idx + 2)
    pass 

# Testing the function
print(recursiveSumEven([1, 2, 3, 4, 5, 6])) # Expected output: 9
print(recursiveSumEven([2, 3])) # Expected output: 2
print(recursiveSumEven([])) # Expected output: 0