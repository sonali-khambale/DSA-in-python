# frequency hashing for character
s = 'azyxyyzaaa'
q = ['a','a','y','x']

# Step 1: create hash list
hash_list = [0] * 26

# Step 2: store frequency
for ch in s:
    index = ord(ch) - ord('a')
    hash_list[index] += 1

# Step 3: query
for ch in q:
    index = ord(ch) - ord('a')
    print(hash_list[index])
