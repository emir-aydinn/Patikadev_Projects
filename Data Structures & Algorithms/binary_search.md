# Binary Search Tree
## Question
[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] write the Binary-Search-Tree steps.



### Solution
While creating a Binary Search tree, bigger values are at the right side and smaller values are at the left side of the nodes. In our case number 7 is determined as root node.
```
 
              7

```
```
              7
             /
            5   
                  
```
```
              7
             /
            5
           /
          1                 
```
```
              7
             / \
            5   8
           /
          1 
```             
```            
              7
             / \
            5   8
           / 
          1   
           \
            3
```
```                 
              7
             / \
            5   8
           / \
          1   6
           \
            3          
```
```                          
              7
             / \
            5   8     
           / \
          1   6
         / \
        0   3    
```
```  

              7
             / \
            5   8
           / \   \
          1   6   9
         / \                   
        0   3            
```
```
              7
             / \
            5   8
           / \   \ 
          1   6   9
         / \
        0   3
             \
              4
```
```
              7
             / \
            5   8
           / \   \ 
          1   6   9
         / \
        0   3
           / \
          2   4
```
