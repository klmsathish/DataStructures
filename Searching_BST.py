import timeit
start = timeit.timeit()
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            temp = self.root
            while True:
                if (temp.data >= val):
                    if (temp.left == None):
                        temp.left = Node(val)
                        break
                    else:
                        temp = temp.left
                elif (temp.data < val):
                    if (temp.right == None):
                        temp.right = Node(val)
                        break
                    else:
                        temp = temp.right

    def Preorder(self, node):
        if (node == None):
            return
        else:
            print(node.data, end=" ")
            self.Preorder(node.left)
            self.Preorder(node.right)
    def Inorder(self, node):
        if (node == None):
            return
        else:
            self.Inorder(node.left)
            print(node.data, end=" ")
            self.Inorder(node.right)

    def Postorder(self, node):
        if (node == None):
            return
        else:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node.data, end=" ")
def search(root, key):
    if (root == None):
        return False
    if (root.data == key):
        return True
    if root.data < key:
        return search(root.right, key)
    else:
        return search(root.left, key)
tree = BinarySearchTree()
n = int(input("how many elements"))
for i in range(n):
    data = (int(input("enter data: ")))
    tree.insert(data)
if search(tree.root, 452):
    print("Found")
else:
    print("The Element You Are searching Not found")
end = timeit.timeit()
time = end -start
