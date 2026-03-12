
def in_to_cm(value):
       return round(value * 2.54, 2)

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


def average_precipitation(data):
        sum = 0
        i = 0 
        average = 0
        for value in data.values():
                sum += value
                i += 1

        if i == 0:
                return False 
        else: 
                average = sum/i 
        return average


def positive_deviations(data):
        above_mean_count = 0

        for value in data.values():
                if value  > average_precipitation(data):
                        above_mean_count += 1
        return above_mean_count 

                
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
                  

    

