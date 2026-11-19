

# a1 = [1,45,32,42,7,87,11,23,10]
# a2 = [11,23,55,66,44,8,33,22]
# a3 = []

# for i,j in zip(a1,a2):
#     a3.append(i)
#     a3.append(j)
#     for a in range(len(a3)):
#         for b in range(a+1,len(a3)):
#             if a3[a] > a3[b]:
#                 a3[a],a3[b] = a3[b],a3[a]

# print(a3)


# xr = [1,23,44,56,76,87,90,100]
# yr = [5,22,34,43,55,66,77,87,109]

def merge(ar,br):
    i = 0
    j = 0
    cr =[]
    while i<len(ar) and j<len(br):
        if ar[i] <= br[j]:
            cr.append(ar[i])
            i+=1
        else:
            cr.append(br[j])
            j+=1
    cr.extend(ar[i:])
    cr.extend(br[j:]) 
    return cr
    

def mergesort(ar,width):
    res = []
    for i in range(0,len(ar), width*2):
        leftarr = ar[i:i+width]
        rightarr = ar[i+width:i+width*2]
        res.extend(merge(leftarr,rightarr))
    return res


xr = [9,4,23,12,5,76,75,43,39,85]

width = 1
while width <len(xr):
    xr = mergesort(xr,width)
    # print(xr)
    width *=2

print(xr)   