class BST:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
    def insert(self,data):
        if self.value:
            if data<self.value:
                if self.left is None:
                    self.left=BST(data)
                else:
                        self.left.insert(data)
            elif data>self.value:
                if self.right is None:
                    self.right=BST(data)
                else:
                    self.right.insert(data)
        else:
            self.value=data
    def search(self,data):
        if self.value==data:
            print("Node is found")
            return
        if data<self.value:
            if self.left:
               self.left.search(data)
            else:
              print("Node is not present in tree")
        else:
             if self.right:
                self.right.search(data)
             else:
                print("Node is not present in tree")
root=BST(10)
list=[20,30,4,50,6]
for i in list:
     root.insert(i)
root.search(6)
root.search(35)

                

    
                                        
