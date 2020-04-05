A = []
x=int(input("enter the size of array:"))
for  i in range(x):
    b=int(input("Enter the number:"))
    A.append(b)
# Traverse through all array elements 
for i in range(0,len(A)): 
    smallest=min(A[i:])
    min_indx=A.index(smallest)
    A[i],A[min_indx]=A[min_indx],A[i]
print("sorted array:")
print(A)

def selection_sort(alist):
    for i in range(0, len(alist)):
        smallest = i
        for j in range(i, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('Sorted list: ', end='')
print(alist)
