# TC: O(n + maxNumber), SC: O(maxNumber)
# in-place, not stable
def countingSort(arr):
    n = len(arr)
    maxNum = max(arr)
    freq = [0] * (maxNum + 1)
    for i in range(len(arr)):
        freq[arr[i]] += 1
    res = [0] * n
    i = 0
    for currNum, currNumFreq in enumerate(freq):
        for _ in range(currNumFreq):
            res[i] = currNum
            i += 1