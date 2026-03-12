import random

def merge_sort(arr):
    if len(arr) > 1:    # If array size is one, do nothing
        left_arr = arr[:len(arr)//2] # Creates slices of array, starting at index 0 to index array divide by 2 (midpoint)
        right_arr = arr[len(arr)//2:] # Creates slices of array, starting at middle to the end of remaining of array
    
    # recursion calls
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge left and right array
        i = 0 # keeps track of left_arr index
        j = 0 # keeps track of right_arr index
        k = 0 # keeps track of merged array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]: # Base case - Left Array index < Right Array index
                arr[k] = left_arr[i]       # Save value relating to Left Array Index to Merge Array 
                i += 1                     
            else:                         
                arr[k] = right_arr[j]      # Case 2 - Right Array index <= Left Array Index
                j += 1      
            k += 1
        
        while i < len(left_arr):           # Case 3 - Transfer all sorted Left Array elements to Merge Array
            arr[k] = left_arr[i]
            i += 1
            k += 1
    
        while j < len(right_arr):         # Case 4 - Check if at end of Right Array, then assign every element to Merge Array
            arr[k] = right_arr[j]
            j+= 1
            k+= 1
# End of Merge Sort Algorithm
"""
test_arr = [2,3,5,1,7,4,4,4,2,6,0] # Simple Test Array
merge_sort(test_arr)               # Calls merge_sort function 
print(test_arr)                    # Prints results
"""
# Simple line break between print results, make out put look cleaner
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
random_test_arr1 = [random.randint(-1000000,1000000) for int in range(10)] # Random 10 Int Array Between - Million to + Million
print("\nRandom Unsorted Test Array from range negative million to positive million:"
"", random_test_arr1)

(merge_sort(random_test_arr1))

print("\nRandom Sorted Test Array from range negative million to positive million:"
"", random_test_arr1, "\n")

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
random_test_arr2 = [random.randint(-10000,10000) for int in range(10)] # Random 10 Int Array Between - Ten Thousand to + Ten Thousand
print("\nRandom Unsorted Test Array from range negative ten thousand to positive ten thousand:"
"", random_test_arr2)

(merge_sort(random_test_arr2))

print("\nRandom Sorted Test Array from range negative ten thousand to positive ten thousand:"
"", random_test_arr2 , "\n")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
random_test_arr3 = [random.randint(-1000,1000) for int in range(10)] # Random 10 Int Array Between - Thousand to + Thousand
print("\nRandom Unsorted Test Array from range negative thousand to positive thousand:"
"", random_test_arr3)

(merge_sort(random_test_arr3))

print("\nRandom Sorted Test Array from range negative thousand to positive thousand:"
"", random_test_arr3, "\n")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
random_test_arr4 = [random.randint(-10,10) for int in range(10)] # Random 10 Int Array Between - Ten to + Ten
print("\nRandom Unsorted Test Array from range negative ten to positive ten:"
"", random_test_arr4)

(merge_sort(random_test_arr4))

print("\nRandom Sorted Test Array from range negative ten to positive ten:"
"", random_test_arr4, "\n")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
