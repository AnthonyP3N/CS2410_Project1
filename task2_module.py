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






# Function to easily convert inches to centimeters, use round to keep numbers readable, converts value to float at decimal point 2
def in_to_cm(value):
       return round(value * 2.54, 2)

# Function to calculate max value of precipitation (month:rainfall)
def maximum_precipitation(data):

        max_value = None 
        max_key = None

        for key, value in data.items(): # Base Case : If dictionary only has one key-value pair
                max_value = value
                max_key = key
                break
        
        for key, value in data.items():         # Case 2 : Continues if dictionary has multiple key-value pair(s)
                if value > max_value:           # Tests current value verus current max
                        max_value = value       # Updates if current value is greater than current max value
                        max_key = key


        return max_key, in_to_cm(max_value)             # Returns max value


# Function to calculate min value of precipitation (month:rainfall)
def minimum_precipitation(data):
        
        min_value = None
        min_key = None

        for key, value in data.items():
                min_value = value
                min_key = key
                break

        for key, value in data.items():
                if value < min_value:
                        min_value = value
                        min_key = key

        return min_key, in_to_cm(min_value)       

# Function to calculate average of total of all precipitation (total/i = average)
def average_precipitation(data):

        total = 0
        i = 0 
        average = 0

        for value in data.values():
                total += value
                i += 1

        if i == 0:
                return None 
        else: 
                average = total/i 
                
        return average

# Function to count total amount of months above average/mean
def positive_deviations(data):
        above_mean_count = 0

        for value in data.values():
                if value  > average_precipitation(data):
                        above_mean_count += 1
        return above_mean_count 

# Function for reverse bubble sort                
def reverse_bubble_sort(data):
    convert_dict = {}
    for key in data:
           convert_dict[key] = in_to_cm(data[key])

    # Convert dictionary items to a list of tuples (key, values)
    items = list(convert_dict.items())
    n = len(items)

    # Outer loop for passes
    for i in range(n - 1):
        # Inner loop for comparisons and swaps
        for j in range(0, n - i - 1):
            # Compare based on the value (index 1 of the tuple)
            if items[j][1] < items[j + 1][1]:
                # Swap the elements if they are in the wrong order
                items[j], items[j + 1] = items[j + 1], items[j]
                
    # Convert the sorted list of tuples back to a dictionary
    return dict(items)
                  

    

