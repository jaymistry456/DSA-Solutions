# TC: O(nlogn), SC: O(n)
# not in-place, stable
def merge(arr, l, mid, r):
    res = []
    i = l
    j = mid + 1
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1
    res.extend(arr[i:mid+1])
    res.extend(arr[j:r+1]) 
    for i in range(l, r + 1):
        arr[i] = res[i - l]
    return res

def mergeSort(arr, l, r):
    if r - l + 1 <= 1:
        return arr
    mid = l + (r - l) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    merge(arr, l, mid, r)
    return arr