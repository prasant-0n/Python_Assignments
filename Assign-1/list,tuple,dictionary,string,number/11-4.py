# Find the letter used maximum and minimum time in a string

test_str = input('enter a string- ')

all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
max_Str = max(all_freq, key=all_freq.get)
min_Str = min(all_freq, key=all_freq.get)


print(f"The maximum charector of String{test_str} is : {str(max_Str)}")
print(f"The minimun charector of String{test_str} is : {str(max_Str)}")
