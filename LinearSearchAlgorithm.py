def search(list,n): 
  
    for i in range(len(space)): 
        if space[i] == n: 
            return True
    return False
space = []
ran= int(input("Enter number of elements: "))
for i in range(ran):
    list = int(input("Enter the number : "))
    space.append(list)
n = int(input("Enter the number to search:"))
if search(list, n): 
    print("Found on position") 
else:
    print("Not Found") 
