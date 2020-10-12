def qsort(nstart ,nend):
    if nstart >= nend:
        return
    l = nstart
    r = nend
    x = s[(l+r)//2]
    while l <= r:
        while s[l] < x:
            l += 1
        while s[r] > x:
            r = r - 1
        if l <= r:
            s[l], s[r] = s[r] ,s[l]
            l += 1
            r -= 1
    qsort(nstart,r)
    qsort(l,nend)   

def quicksort(list):
    nend = len(list) - 1
    qsort(0, nend)


