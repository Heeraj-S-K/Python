#To Find Extra Occurences

from collections import Counter
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 2, 3, 4, 4, 5]
extra = list((Counter(list2) - Counter(list1)).elements())
print(extra)
