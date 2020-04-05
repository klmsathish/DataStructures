# Node class
class node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
# Linked List class
class LinkedList:
    # Function to initialize the Linked List object

    def __init__(self):
        self.top = None

    def ins(self, val):
        if self.top == None:
            self.top = node(val)
        else:
            temp = self.top
            self.top = node(val)
            self.top.next = temp

    def display(self):
        temp = self.top
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

    def pop(self): 
        poppednode = self.top 
        self.top = self.top.next
         
        return poppednode.data 

        
a_list = LinkedList()
n = int(input("how many elements"))
for i in range(n):
    data = (int(input("enter data: ")))
    a_list.ins(data)

print("linked list = ",end="")
a_list.pop()
a_list.display()
