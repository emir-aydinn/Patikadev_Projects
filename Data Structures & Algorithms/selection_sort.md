# Selection Sort
## Question-1
[22,27,16,2,18,6] -> Insertion Sort

Explain the sorting algorithm above for the given array.
## Solution
### Insertion Sort is an sorting algorithm to sort arrays into descending or ascendig order. Here is the stages:

Given array: [22, 27, 16, 2, 18, 6]\
=>: [22, 27, 16, 2, 18, 6] (first element is considered as sorted)\
=>: [22, 27, 16, 2, 18, 6] (the element at index 1 changes position with the element at index 0 due to being greater)\
=>: [16, 22, 27, 2, 18, 6] (16 is compared with the elements at left and changes position if it is greater)\
=>: [2, 22, 27, 16, 18, 6] (we do this until we put the smallest number at the index 0)\
.\
.\
.\
=>: [2, 6, 27, 22, 18, 16] (we start searching for the smallest number among the remaining list of numbers and put it at index 1)\
=>: [2, 18, 6, 16, 22, 27] (we repeat this process until there is no left number to be sorted)\

Sorted array: [2, 6, 16, 18, 22, 27]

## Question-2
Write the Big-O notation.
## Solution
Big-O Notation:  O(n^2) 

## Question-3
Time Complexity: After sorting the array, which case describes best searching number 18? Write it down...
1. Average case: The searched number is at the middle
2. Worst case: The searched number is at the end
3. Best case: The searched number is at the begining of the array

## Solution
Number 18 is the 4th element of the array, for that reason having a search with average case is more advantageous.
