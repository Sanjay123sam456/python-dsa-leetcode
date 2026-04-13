nums = [1,2,3,2,1,3,3,4]

# Step 1: frequency
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Step 2: find most frequent
most_freq = nums[0]

for key in freq:
    if freq[key] > freq[most_freq]:
        most_freq = key

print("Most frequent:", most_freq)
