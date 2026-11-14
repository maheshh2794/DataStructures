# def febo(n):
#     if n == 0:
#         return 0
#     if n ==1:
#         return 1
#     return febo(n-1) + febo(n-2)

# print(febo(5))


def febSeries(n, a=0, b=1):
    if n == 0:
        return

    print(a, end=" ")
    febSeries(n-1, b, a+b)

febSeries(10)