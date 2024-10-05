def quicksort(arr):
  """Sorts an array using the Quicksort algorithm.

  Args:
    arr: The array to be sorted.

  Returns:
    The sorted array.
  """

  if len(arr) <= 1:
    return arr

  pivot = arr[0]
  left = []
  right = []

  for num in arr[1:]:
    if num < pivot:
      left.append(num)
    else:
      right.append(num)

  return quicksort(left) + [pivot] + quicksort(right)

# Example usage
array = [5, 2, 8, 1, 9, 3]
sorted_array = quicksort(array)
print(sorted_array)  # Output: [1, 2, 3, 5, 8, 9]
