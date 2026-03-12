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