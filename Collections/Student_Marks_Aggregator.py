#Group by marks

from collections import defaultdict
data = [("Alice", 85), ("Bob", 78), ("Alice", 92), ("Bob", 88)]
d = defaultdict(list)
for name, marks in data:
    d[name].append(marks)
print(dict(d))
