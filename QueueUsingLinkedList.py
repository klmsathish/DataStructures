class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:   
    def __init__(self):
        self.head = None
        self.last_node = None
    def Enqueue(self,data):
        newnode = Node(data)
        if self.last_node == None:
            self.head = newnode
            self.last_node = self.head
            return
        else:
            self.last_node.next = newnode
            self.last_node = newnode
    def Dequeue(self):
        if self.head is None:
            return
        current = self.head
        self.front = current.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data,end = " ")
            current = current.next
queue = LinkedList()
n = int(input("how many elements"))
for i in range(n):
    data = (int(input("enter data: ")))
    queue.Enqueue(data)

print("linked list = ",end="")
queue.display()





