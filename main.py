# import calls
import task2_module as mod                          # import module file, please have file in same folder/file path as main.py
import pprint                                       # import pretty print method
import random                                       # import random function to use 


# -----Task 1 Code-----
"""
test_arr = [2,3,5,1,7,4,4,4,2,6,0] # Simple Test Array
merge_sort(test_arr)               # Calls merge_sort function 
print(test_arr)                    # Prints results
"""

print("\nTask 1 Code Output:")

# Simple line break between print results, make out put look cleaner
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

#
# Random 10 Int Array Between - Million to + Million
#
random_test_arr1 = [random.randint(-1000000,1000000) for int in range(10)] 
print("\nRandom Unsorted Test Array from range negative million to positive million:"
"", random_test_arr1)

(mod.merge_sort(random_test_arr1))

print("\nRandom Sorted Test Array from range negative million to positive million:"
"", random_test_arr1, "\n")

#
# Random 10 Int Array Between - Ten Thousand to + Ten Thousand
#
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
random_test_arr2 = [random.randint(-10000,10000) for int in range(10)] 
print("\nRandom Unsorted Test Array from range negative ten thousand to positive ten thousand:"
"", random_test_arr2)

(mod.merge_sort(random_test_arr2))

print("\nRandom Sorted Test Array from range negative ten thousand to positive ten thousand:"
"", random_test_arr2 , "\n")

#
# Random 10 Int Array Between - Thousand to + Thousand
#
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
random_test_arr3 = [random.randint(-1000,1000) for int in range(10)] 
print("\nRandom Unsorted Test Array from range negative thousand to positive thousand:"
"", random_test_arr3)

(mod.merge_sort(random_test_arr3))

print("\nRandom Sorted Test Array from range negative thousand to positive thousand:"
"", random_test_arr3, "\n")

#
# Random 10 Int Array Between - Ten to + Ten
#
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
random_test_arr4 = [random.randint(-10,10) for int in range(10)] 
print("\nRandom Unsorted Test Array from range negative ten to positive ten:"
"", random_test_arr4)

(mod.merge_sort(random_test_arr4))

print("\nRandom Sorted Test Array from range negative ten to positive ten:"
"", random_test_arr4, "\n")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# -----End of Task 1 Code-----


# -----Task 2 Code-----
            #  Month|Rainfall (in)
rainfall_dict= {"01":133.5,
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

print("\nTask 2 Code Output:")

# Calls function maximum_precipitatoin from module file
max = mod.maximum_precipitation(rainfall_dict)
print("The month observed to have the maximum precipitation level is: (units:cm)\n", max, "\n")

# Calls function minimum_precipitatoin from module file
min = mod.minimum_precipitation(rainfall_dict)
print("The month observed to have the minimum precipitation level is: (units:cm)\n", min, "\n")

# Calls function average_precipitatoin from module file
avg = mod.average_precipitation(rainfall_dict)

# Calls function inches to centimeters separately to not affect function positive_deviations
avg = mod.in_to_cm(avg)                                  

print("The average of all the recorded precipitation levels is", avg, "cms. \n")

# Calls function positive_deviations from module file (total amount of values > mean)
above_mean = mod.positive_deviations(rainfall_dict)
print("The total amount of months with greater levels of precipitation than average is",above_mean, "\n")

# Calls function reverse_bubble_sort from module file
rbs = mod.reverse_bubble_sort(rainfall_dict)
print("The descending order of precipitation observed is as seen: (units:cm)\n",rbs, "\n")


print("The descending order of precipitation observed is as seen:(using pprint for formatting) (units:cm)")
# Utilize built in python method pretty print to format dict better, makes it more readable, doesn't actually sort anything 
pprint.pprint( rbs, sort_dicts = False,width=1)





# Below are the test dictionaries used

# Large values with a single zero
test_dict1 = {"01":0,
              "02":670391,
              "03":8932032,
              "04":32,
              "05":2343}

# Large negative values with two zeros
test_dict2 = {"01":0,
              "02":0,
              "03":-10000,
              "04":32,
              "05":-2343}

# A dictionary of all zeros
test_dict3 = {"01":0,
              "02":0,
              "03":0,
              "04":0,
              "05":0}
# The code below is to test the test dictionaries above 
# Delete """""" to test fully
"""
print("\n..............Testing with Data Set 1 ..............\n")
max = mod.maximum_precipitation(test_dict1)
print("The month observed to have the maximum precipitation level is: (units:cm)\n", max, "\n")

min = mod.minimum_precipitation(test_dict1)
print("The month observed to have the minimum precipitation level is: (units:cm)\n", min, "\n")

avg = mod.average_precipitation(test_dict1)
avg = mod.in_to_cm(avg)
print("The average of all the recorded precipitation levels is", avg, "cms. \n")

above_mean = mod.positive_deviations(test_dict1)
print("The total amount of months with greater levels of precipitation than average is",above_mean, "\n")

rbs1 = mod.reverse_bubble_sort(test_dict1)
print("The descending order of precipitation observed is as seen: (units:cm)\n",rbs1, "\n")

print("The descending order of precipitation observed is as seen:(using pprint for formatting) (units:cm)")
pprint.pprint( rbs1, sort_dicts = False, width=1)


print("\n..............Testing with Data Set 2 ..............\n")
max = mod.maximum_precipitation(test_dict2)
print("The month observed to have the maximum precipitation level is: (units:cm)\n", max, "\n")

min = mod.minimum_precipitation(test_dict2)
print("The month observed to have the minimum precipitation level is: (units:cm)\n", min, "\n")

avg = mod.average_precipitation(test_dict2)
avg = mod.in_to_cm(avg)
print("The average of all the recorded precipitation levels is", avg, "cms. \n")

above_mean = mod.positive_deviations(test_dict2)
print("The total amount of months with greater levels of precipitation than average is",above_mean, "\n")

rbs2 = mod.reverse_bubble_sort(test_dict2)
print("The descending order of precipitation observed is as seen: (units:cm)\n",rbs1, "\n")

print("The descending order of precipitation observed is as seen:(using pprint for formatting) (units:cm)")
pprint.pprint( rbs2, sort_dicts = False, width=1)


print("\n..............Testing with Data Set 3 ..............\n")
max = mod.maximum_precipitation(test_dict3)
print("The month observed to have the maximum precipitation level is: (units:cm)\n", max, "\n")

min = mod.minimum_precipitation(test_dict3)
print("The month observed to have the minimum precipitation level is: (units:cm)\n", min, "\n")

avg = mod.average_precipitation(test_dict3)
avg = mod.in_to_cm(avg)
print("The average of all the recorded precipitation levels is", avg, "cms. \n")

above_mean = mod.positive_deviations(test_dict3)
print("The total amount of months with greater levels of precipitation than average is",above_mean, "\n")

rbs3 = mod.reverse_bubble_sort(test_dict3)
print("The descending order of precipitation observed is as seen: (units:cm)\n",rbs3, "\n")

print("The descending order of precipitation observed is as seen:(using pprint for formatting) (units:cm)")
pprint.pprint( rbs3, sort_dicts = False, width=1)
"""