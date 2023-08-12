
# Defining a function called "reverse" to order the given input list as its reverse...
def reverse(n):
 n = n[::-1]
 n = [m[::-1] for m in n]
 return n

input_list=[[1, 2], [3, 4], [5, 6, 7]]

print("Original list: ")
print(input_list)
print("Reversed list: ")
print(reverse(input_list))