import time
import random


def bubble_sort(arr):
    n = len(arr)
    for p in range(n-1):
        swapped = False
        for i in range(n-p-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Iterate through the entire array
    for i in range(n):
        # Assume the current position has the minimum value
        min_index = i
        
        # Search for the minimum element in the unsorted portion of the array
        for j in range(i+1, n):
            # If we find a smaller element, update min_index to its position
            if arr[j] < arr[min_index]:
                min_index = j
        
        # After finding the minimum element, swap it with the element at position i
        # This places the minimum element in its correct sorted position
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    # Return the sorted array
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """Binary search implementation for sorted arrays"""
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 📌 Function to test sorting performance
def test_sorting_performance():
    """
    Generates lists of random numbers and tests the execution time of sorting and search algorithms.
    """
    small_dataset = [random.uniform(1, 100) for _ in range(50)]
    large_dataset = [random.uniform(1, 100) for _ in range(1000)]
    larger_dataset = [random.uniform(1, 100) for _ in range(10000)]
    
    print("\n🔹 Small Dataset (50 elements):")
    
    # Bubble Sort test
    bubble_test = small_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"✅ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = small_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")

    # Insertion Sort test
    insertion_test = small_dataset.copy()
    start_time = time.time()
    insertion_sort(insertion_test)
    end_time = time.time()
    print(f"✅ Insertion Sort took {end_time - start_time:.6f} seconds.")

    # Linear Search test
    linear_search_test = small_dataset.copy()
    start_time = time.time()
    linear_search(linear_search_test, 50)
    end_time = time.time()
    print(f"✅ Linear Search took {end_time - start_time:.6f} seconds.")
    
    print("\n🔹 Large Dataset (1000 elements):")

    # Insertion Sort test
    insertion_test = large_dataset.copy()
    start_time = time.time()
    insertion_sort(insertion_test)
    end_time = time.time()
    print(f"✅ Insertion Sort took {end_time - start_time:.6f} seconds.")
    
    # Bubble Sort test
    bubble_test = large_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"⚠️ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = large_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")

    # Linear Search test
    linear_search_test = large_dataset.copy()
    start_time = time.time()
    linear_search(linear_search_test, 50)
    end_time = time.time()
    print(f"✅ Linear Search took {end_time - start_time:.6f} seconds.")
    
    # Python Built-in Sort
    python_sort_test = large_dataset.copy()
    start_time = time.time()
    sorted(python_sort_test)
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")
    
    print("\n🔹 Larger Dataset (10000 elements):")
    
    # Python Built-in Sort (test this first as it's fastest)
    python_sort_test = larger_dataset.copy()
    start_time = time.time()
    sorted_dataset = sorted(python_sort_test)
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")
    
    # Insertion Sort test
    insertion_test = larger_dataset.copy()
    start_time = time.time()
    insertion_sort(insertion_test)
    end_time = time.time()
    print(f"⚠️ Insertion Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = larger_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"⚠️ Selection Sort took {end_time - start_time:.6f} seconds.")
    
    # Bubble Sort test - might be very slow, so we'll warn about it
    print("⚠️ Bubble Sort may take a long time on 10,000 elements...")
    bubble_test = larger_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"⚠️ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Linear Search test
    linear_search_test = larger_dataset.copy()
    start_time = time.time()
    linear_search(linear_search_test, 50)
    end_time = time.time()
    print(f"✅ Linear Search took {end_time - start_time:.6f} seconds.")
    
    # Binary Search test (on sorted array)
    binary_search_test = sorted_dataset.copy()  # Use the already sorted dataset
    start_time = time.time()
    binary_search(binary_search_test, 50)
    end_time = time.time()
    print(f"🚀 Binary Search took {end_time - start_time:.6f} seconds.")


# Run the performance test
test_sorting_performance()

# Analysis and Conclusions:
# 1. Small datasets (50 elements):
#    - All sorting algorithms perform similarly
#    - Differences are negligible for practical purposes
#
# 2. Medium datasets (1000 elements):
#    - Bubble Sort shows significant slowdown
#    - Selection Sort performs better than Bubble Sort but still not efficient
#    - Insertion Sort is generally faster than both Bubble and Selection Sort
#    - Python's built-in sort is dramatically faster than all three
#
# 3. Large datasets (10000 elements):
#    - O(n²) algorithms (Bubble, Selection, Insertion) become very inefficient
#    - Bubble Sort is the slowest due to excessive swapping operations
#    - Python's built-in sort (Timsort - O(n log n)) is dramatically faster
#    - Binary search is much faster than linear search on sorted arrays
