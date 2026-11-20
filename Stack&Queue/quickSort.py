
from turtle import right


def quickSort(ar):
    a = 0
    b = 0
    pv = len(ar)-1

    if len(ar) <= 1:
        return ar

    while a < len(ar):
        if a == pv:
            ar[b],ar[pv] = ar[pv],ar[b]
            break
        if ar[a] < ar[pv]:
            ar[a],ar[b] = ar[b],ar[a]
            a+=1
            b+=1
        # elif ar[a]==ar[pv]:
        #     a+=1
        #     b+=1
        else:
            a+=1

    left_arr = quickSort(ar[:b])
    right_arr = quickSort(ar[b+1:])
    return left_arr + [ar[b]] + right_arr

xr = [7,2,9,4,1,6,3,5]
print(quickSort(xr))
         
        