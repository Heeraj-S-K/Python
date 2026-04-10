#To group words by length
from collections import defaultdict
words = ["python", "java", "go", "c", "ruby", "php"]
d = defaultdict(list)
for word in words:
    d[len(word)].append(word)
print(dict(d))
