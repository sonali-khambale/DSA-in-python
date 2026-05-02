// frequency of elements using haching of numbers
# Frequency Array / Hash Table Problem
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0]*11

# Step 1: store frequency 
for num in n:
    hash_list[num] += 1

# Step 2: Query using m
for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])
