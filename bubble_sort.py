# O(n^2) algo

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

array = [3, 4, 2, 5, 0, 1, 2, 7, 6]
bubble_sort(array)
print(array)