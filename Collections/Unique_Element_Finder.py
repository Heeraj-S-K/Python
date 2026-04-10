# TO FIND UNIQUE ELEMENTS
from collections import Counter
nums = [5, 3, 5, 2, 3, 1, 4, 1, 2]
count = Counter(nums)
unique = [num for num in count if count[num] == 1]
print(unique)
