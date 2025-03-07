import time
import random


def bubble_sort(arr):
   n = len(arr)
   l = n #initializing the length of the array
   p = 1#pas the counter
   while p<= n-1:
       e = 0#intialize exchange counter
       for i in range(l-1):
           if arr[i]>arr[i+1]:
               arr[i],arr[i+1] = arr[i+1],arr[i]#swap the elements
               e+=1
       if e == 0:
        break#if no exchange is made, the array is sorted
       l -=1#reduce the length of the array
       p+=1#move to the next pass
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

# 📌 Function to test sorting performance
def test_sorting_performance():
    """
    Generates a list of random numbers and tests the execution time of both sorting algorithms.
    """
    small_dataset = [random.uniform(1, 100) for _ in range(50)]
    large_dataset = [random.uniform(1, 100) for _ in range(1000)]
    
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
    
    print("\n🔹 Large Dataset (1000 elements):")
    
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
    
    # Python Built-in Sort
    python_sort_test = large_dataset.copy()
    start_time = time.time()
    sorted(python_sort_test)
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")

# Run the performance test
test_sorting_performance()

#Analysis and Conclusions :
#bubble sort and selection are similar on small datasets
#bBubble Sort performs poorly on large datasets due to its O(n²) time complexity
#Selection Sort is slightly better than Bubble Sort, but still not efficient for large datasets
