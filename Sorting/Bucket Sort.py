# TC: O(n + maxNumber), SC: O(maxNumber)
# in-place, not stable
def bucketSort(arr, maxNumber):
    n = len(arr)
    freq = [0] * (maxNumber + 1)
    for i in range(n):
        freq[arr[i]] += 1
    i = 0
    for j in range(maxNumber + 1):
        for _ in range(freq[j]):
            arr[i] = j
            i += 1
    return arr