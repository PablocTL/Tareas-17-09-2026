def insertion_sort(arr):
    for i in range(1,len(arr)):
        pos = arr[i]
        j = i-1
        while j >= 0 and pos < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pos
    return arr

arr = [1,5,4,7,9,10,17,3]
print(insertion_sort(arr))
