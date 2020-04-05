# Node class 
class Node: 
	# Function to initialize the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 
# Linked List class 
class LinkedList: 
	# Function to initialize the Linked List object 
	def __init__(self): 
		self.head = None
		self.last_node = None
	# Function to append values
	def append(self,data):
		# checking whether linked list is none
		if self.head is None:
    		#NewNode = Node(data)
			#self.head = NewNode
			self.head = Node(data)
			self.last_node = self.head
		# then appending for consequent nodes at last
		else:
			self.last_node.next = Node(data)
			self.last_node=self.last_node.next
	def display(self):
		current = self.head
		while current is not None:
			print(current.data)
			current = current.next
			
        
a_list = LinkedList()
n = int(input("how many elements"))
for i in range (n):
	data = (int(input("enter data: ")))
	a_list.append(data)
print("linked list = ")	
a_list.display()
