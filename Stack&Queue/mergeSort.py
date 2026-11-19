
def merge(ar,br):
    cr = []
    i = 0
    j = 0
    while i<len(ar) and j<len(br):
        if ar[i] <= br[j]:
            cr.append(ar[i])
            i +=1
        else:
            cr.append(br[j])
            j+=1
    if i<len(ar):
        cr.extend(ar[i:])
    if j<len(br):
        cr.extend(br[j:])

    return cr

def mergePairs(ar, width):
    cr = []
    for i in range(0, len(ar), 2*width):
        tr = merge(ar[i:i+width],ar[i+width:i+(2*width)])
        cr.extend(tr)
    return cr

xr = [187,43,13,79,43,567,32,76,332,23]
width = 1
while width < len(xr):
    xr = mergePairs(xr,width)
    print(xr)
    width *= 2

print(mergePairs(xr,width))


    
# xr = [4, 12, 17, 22, 32, 34, 64, 67, 77, 86, 99]
# yr = [12, 21, 23, 38, 43, 45, 56, 65]

# print(merge(xr,yr))