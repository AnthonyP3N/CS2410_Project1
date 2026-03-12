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

test_arr = [2,3,5,1,7,4,4,4,2,6,0] # Simple Test Array
merge_sort(test_arr)               # Calls merge_sort function 
print(test_arr)                    # Prints results