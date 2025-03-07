Sorting Algorithms: Bubble Sort & Selection Sort
📖 Overview
This project compares the performance of two fundamental sorting algorithms—Bubble Sort and Selection Sort. The objective is to implement both algorithms to sort a list of product weights, measure their execution times, and analyze their efficiency on small and large datasets. Additionally, we will compare the performance of these algorithms against Python's built-in sorting function.

📝 Objective
The goal of this project is to:

Implement Bubble Sort and Selection Sort algorithms.
Measure the execution time of these sorting algorithms on small and large datasets.
Compare their efficiency with Python's built-in sorting function.
Understand the performance differences between the two sorting methods.
🚀 Features
Bubble Sort: An elementary algorithm that sorts by repeatedly comparing adjacent elements and swapping them if they are in the wrong order.
Selection Sort: An algorithm that works by repeatedly finding the smallest element in the unsorted portion of the list and moving it to its correct position.
Performance Comparison: Execution time measurement of both sorting algorithms for datasets of different sizes (50 and 1000 elements).
Built-in Python Sort: Comparison with Python's highly optimized built-in sorting function (sorted()).
🏆 Learning Outcomes
By completing this project, you will:

Understand how Bubble Sort and Selection Sort work.
Implement sorting algorithms from scratch.
Compare the performance of sorting algorithms.
Gain insight into the real-world implications of algorithmic efficiency.
⚡ Dataset
Two datasets are generated for performance testing:

Small Dataset: 50 randomly generated product weights.
Large Dataset: 1000 randomly generated product weights.
The weights are randomly generated in the range between 1 and 100.

📋 Instructions
1. Bubble Sort
Bubble Sort works by repeatedly comparing adjacent elements and swapping them if they are in the wrong order. This process continues until no swaps occur, which means the list is sorted.

2. Selection Sort
Selection Sort works by finding the smallest element in the unsorted portion of the list and swapping it with the first unsorted element. This process repeats until the entire list is sorted.

3. Performance Testing
Test Small Dataset: Generate a list of 50 random product weights.
Test Large Dataset: Generate a list of 1000 random product weights.
Measure and compare the execution times of Bubble Sort, Selection Sort, and Python’s built-in sorted() function.
💻 Code Structure
bubble_sort(arr): A function that implements the Bubble Sort algorithm.
selection_sort(arr): A function that implements the Selection Sort algorithm.
test_sorting_performance(): A function to generate random datasets, run both sorting algorithms on them, and measure their execution times.
📊 Example Output
Small Dataset (50 product weights):
mathematica
Copy
✅ Bubble Sort took 0.000245 seconds.
✅ Selection Sort took 0.000197 seconds.
Large Dataset (1000 product weights):
mathematica
Copy
⚠️ Bubble Sort took 0.129456 seconds.
✅ Selection Sort took 0.078943 seconds.
🚀 Python Built-in Sort took 0.000032 seconds.
🧑‍💻 How to Run
Clone this repository to your local machine.
bash
Copy
git clone https://github.com/yourusername/sorting-algorithms.git
Navigate to the project directory.
bash
Copy
cd sorting-algorithms
Run the main.py script to execute the sorting algorithms and performance tests.
bash
Copy
python main.py
🔍 Analysis and Conclusion
Bubble Sort and Selection Sort are both inefficient for large datasets due to their O(n²) time complexity.
Selection Sort tends to perform better than Bubble Sort, but both still struggle with larger datasets.
Python’s built-in sort (Timsort) is highly optimized and outperforms both sorting algorithms for large datasets.
🚧 Limitations
Bubble Sort has a best-case time complexity of O(n) if the list is already sorted, but it still performs poorly with large datasets.
Selection Sort has a time complexity of O(n²), which also makes it inefficient for large datasets.
📚 References
Bubble Sort
Selection Sort
Python Sorted Function
📅 License
This project is licensed under the MIT License - see the LICENSE file for details.
