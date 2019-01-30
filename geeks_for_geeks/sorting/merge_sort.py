
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])

        l = r = 0
        merged = []

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1

        if l == len(left):
            merged.extend(right[r:])
        else:
            merged.extend(left[l:])
        return merged

    return arr
