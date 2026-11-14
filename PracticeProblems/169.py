from typing import Counter


arr = [3,2,3]
n = Counter(arr)
for i,j in enumerate(n):
    print(n[j])