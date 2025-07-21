# TC: O(n^2), SC: O(1)
# in-place, stable
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr