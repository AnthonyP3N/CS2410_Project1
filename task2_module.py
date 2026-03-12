example_dict = {"01":133.5,
                "02":64.3,
                "03":104.4,
                "04":86.3,
                "05":48.5,
                "06":35.4,
                "07":55.3,
                "08":84.9,
                "09":104.5,
                "10":104.4,
                "11":122.6,
                "12":119.5}

def maximum_precipitation(dict):
        max_value = None 

        for value in dict.values(): # Base Case : If dictionary only has one key-value pair
                max_value = value
                break
        
        for value in dict.values():             # Case 2 : Continues if dictionary has multiple key-value pair(s)
                if value > max_value:           # Tests current value verus current max
                        max_value = value       # Updates if current value is greater than current max value

        return max_value                        # Returns max value

max = maximum_precipitation(example_dict)
print(max)

def minimum_precipitation(dict):
        min_value = None

        for value in dict.values():
                min_value = value
                break
        for value in dict.values():
                if value < min_value:
                        min_value = value
        return min_value
min = minimum_precipitation(example_dict)
print(min)

def average_precipitation(dict):
        sum = 0
        i = 0 
        average = 0
        for value in dict.values():
                sum += value
                i += 1

        if i == 0:
                return False 
        else: 
                average = sum/i 
        return average 
avg = average_precipitation(example_dict)
print(avg)

def positive_deviations(dict):
        above_mean_count = 0

        for value in dict.values():
                if value > average_precipitation(dict):
                        above_mean_count += 1
        return above_mean_count 
a_mean = positive_deviations(example_dict)
print(a_mean)
                
def reverse_bubble_sort(d):
    # Convert dictionary items to a list of tuples (key, values)
    items = list(d.items())
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
bub = reverse_bubble_sort(example_dict)
print(bub)                    
    