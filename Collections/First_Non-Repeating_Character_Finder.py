 

from collections import OrderedDict

s = "swiss"

od = OrderedDict()

for ch in s:

    od[ch] = od.get(ch, 0) + 1

for ch in od:

    if od[ch] == 1:

        print(f"First non-repeating: {ch}")

        break
