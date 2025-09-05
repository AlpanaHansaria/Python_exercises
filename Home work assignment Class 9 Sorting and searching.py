#Bubble Sort - bubbles the one largest number to the right in each pass
#Exercise 1: Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if a swap happens in this pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps happened, list is already sorted
        if not swapped:
            break
    return arr

# Example
numbers = [5, 3, 8, 4, 2]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # Output: [2, 3, 4, 5, 8]

#Selection Sort - select minimum element and swaps with the current position
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

#Insertion Sort - builds the final sorted array one item at a time
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)

#Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

#Exercise: Make the merge function
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right


#usage and example
numbers = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(numbers))