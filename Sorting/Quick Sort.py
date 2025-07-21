# TC: O(nlogn), SC: O(1)
# in-place, not stable
def partition(arr, l, r):
    pivot = arr[r]
    start = l
    for i in range(l, r + 1):
        if arr[i] < pivot:
            temp = arr[start]
            arr[start] = arr[i]
            arr[i] = temp
            start += 1
    arr[r] = arr[start]
    arr[start] = pivot
    return start

def quickSort(arr, l, r):
    if r - l + 1 <= 1:
        return arr
    partition_index = partition(arr, l, r)
    quickSort(arr, l, partition_index - 1)
    quickSort(arr, partition_index + 1, r)
    return arr