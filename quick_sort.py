def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
def quick_sort_wrapper(arr):
    quick_sort(arr, 0, len(arr)-1)

array = [3, 4, 2, 5, 0, 1, 2, 7, 6]
quick_sort_wrapper(array)
print(array)