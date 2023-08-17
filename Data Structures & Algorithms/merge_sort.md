# Merge Sort
## Question-1
[16,21,11,8,12,22] -> Merge Sort

Explain the sorting algorithm above for the given array.

### Solution
=>: We divide the array into halves until we have no pairs.\
 [ 16, 21, 11 ]  &emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;[ 8, 12, 22 ] 
 
 [ 16, 21 ]&emsp;|&emsp;[ 11 ]&emsp;&emsp;|&emsp;&emsp;[ 8, 12 ]&emsp;|&emsp; [ 22 ]

 [ 16 ]&emsp;|&emsp;[ 21 ]&emsp;|&emsp;[ 11 ]&emsp;|&emsp;[ 8 ]&emsp;|&emsp;[ 12 ]&emsp;|&emsp;[ 22 ]

=>: We start to sort left and right sides separately and then merge.\
[ 16, 21 ]&emsp;|&emsp;[ 11 ]&emsp;&emsp;|&emsp;&emsp;[ 8 ]&emsp;|&emsp;[ 12, 22 ]

[ 11, 16, 21 ]&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;[ 8, 12, 22 ]


=>: We merge the two halves in order to create a sorted list.\
Merge: [8, 11, 12, 16, 21, 22]


## Question-2
Wrtie down the Big-O notation.
### Solution
Big-O Notation:  O(n log n)