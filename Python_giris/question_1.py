#Defining a function called "flatten(m)" which takes list m object and flattens it in return...
final_list=[]
def flatten(m):
     for i in m:
         if isinstance(i,list):
          flatten(i)
         else:
          final_list.append(i)


input_list=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print("Original list: ")
print(input_list)
print("Flattened list: ")
flatten(input_list)
print(final_list)
