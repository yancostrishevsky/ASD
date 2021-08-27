def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                swap(arr, j, j + 1)
                ifSwapped = True

        if (ifSwapped == False):
            break
    return arr