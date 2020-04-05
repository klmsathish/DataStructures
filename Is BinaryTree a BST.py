class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class bst:
    def __init__(self):
        self.curnode=None

    def insert(self,cn,val):
        if self.curnode==None:
            self.curnode=node(val)
        else:
            if cn==None:
                cn=node(val)
            else:
                if val<cn.data:
                    cn.left=self.insert(cn.left,val)
                elif val>cn.data:
                    cn.right=self.insert(cn.right,val)            
            return cn

    def display(self,cn):
        if self.curnode==None:
            print("List is empty")
        else:
            if cn==None:
                return
            else:
                self.display(cn.left)
                self.display(cn.right)
                print(cn.data,end=" ")

    def isbst(self):
        f1=0
        f2=0
        cn=self.curnode
        while cn!=None:
            if cn.left==None:
                break
            else:
                if cn.data<cn.left.data:
                    f1=1
                    break
                else:
                    cn=cn.left
        while cn!=None:
            if cn.right==None:
                break
            else:
                if cn.right.data<cn.data:
                    f2=1
                    break
                else:
                    cn=cn.right
        if f1==0 and f2==0:
            print("It is a BST")
        else:
            print("It is not a BST")

b=bst()
b.insert(b.curnode,4)
b.insert(b.curnode,2)
b.insert(b.curnode,5)
b.insert(b.curnode,1)
b.display(b.curnode)
print("")
b.isbst()