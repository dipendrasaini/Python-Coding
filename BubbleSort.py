#Python Program for Bubble Sort
 
#Ascending means smallest to largest, 0 to 9
 
#Descending means largest to smallest, 9 to 0
 
#if arr[j] > arr[j + 1]:
#     swapped = True
#     arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
i=0
j=0
 
for i in range(len(arr)-1):
 
# outer loop will invoke inner loop with range of value  
 
  for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)
