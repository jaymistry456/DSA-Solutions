# TC: O(n^2), SC: O(1)
# in-place, not stable ([2, 2, 1])
def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr