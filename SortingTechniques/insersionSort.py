arr = [12,2,11,34,53,5,23,45]

for i in range(len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]

print(arr)

