result = []
current = []

def backtrack(start,nums):
    result.append(current.copy())
    for i in range(start, len(nums)):
        current.append(nums[i])
        backtrack(i+1,nums)
        current.pop()
    return result

n = 0
arr = [1,2,3]
a = backtrack(n,arr)
print(a)
