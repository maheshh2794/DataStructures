
# arr1 = [1,8]
# arr2 = [3,11]
# arr1.extend(arr2)
# print(arr1)


a1 = [1,45,32,42,7,87,11,23,10]
a2 = [11,23,55,66,44,8,33,22]


a3 = []

for i,j in zip(a1,a2):
    a3.append(i)
    a3.append(j)
    for a in range(len(a3)):
        for b in range(a+1,len(a3)):
            if a3[a] > a3[b]:
                a3[a],a3[b] = a3[b],a3[a]

print(a3)





# a1 = [1,45,32,42]
# a2 = [11,23,55,66,44,8,33,22]

# a3 = []

# for i in a1 + a2:
#     j = 0
#     while j < len(a3) and a3[j] < i:
#         j += 1
#     a3.insert(j, i)
# print(a3)