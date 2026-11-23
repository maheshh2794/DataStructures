
def toh(n,s,d,a):
    if n == 1:
        print(f"{n} Moves from {s} to {d}")
        return
    toh(n-1,s,a,d)
    print(f"{n} Moves from {s} to {a}")
    toh(n-1,a,d,s)

toh(3,"A","B","C")