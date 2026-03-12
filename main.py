import task2_module as mod

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

max = mod.maximum_precipitation(rainfall_dict)
print(max)

min = mod.minimum_precipitation(rainfall_dict)
print(min)

avg = mod.average_precipitation(rainfall_dict)
avg = mod.in_to_cm(avg)
print(avg)

above_mean = mod.positive_deviations(rainfall_dict)
print(above_mean)

rbs = mod.reverse_bubble_sort(rainfall_dict)
print(rbs)