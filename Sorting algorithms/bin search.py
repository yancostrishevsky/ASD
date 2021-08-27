def binarySearch(T,beg,end,x):
    if beg > end:
        return None
    mid = (beg + end)//2
    if T[mid] ==x:
        retval  = binarySearch(T,beg,mid-1,x)
        if retval == None:
            return mid
        return retval

    if T[mid] > x:
        return binarySearch(T,beg,mid-1,x)
    else:
        return binarySearch(T,mid+1, end,x)