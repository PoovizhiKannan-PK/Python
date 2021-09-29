class TreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
    
    def addChild(self, data):
        if data == self.data:
            return
        
        elif data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = TreeNode(data)
        
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = TreeNode(data)
    
    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements +=  self.left.inOrderTraversal()
            
        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()
        
        return elements

    def preOderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOderTraversal()
        
        if self.right:
            elements += self.right.preOderTraversal()
        return elements
    
    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements+= self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.data)
        return elements

    def findMin(self):
        if self.left:
            self = self.left
            self.findMin()
            return
        
        print(self.data)

    def findMax(self):
        if self.right:
            self = self.right
            self.findMax()
            return
        
        print(self.data)

def buildTree(elements):
    root = TreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])
    
    return root

if __name__ == "__main__":
    elements = [15,12,23,20,27,88,7,14]
    tree = buildTree(elements)

    print(tree.inOrderTraversal())
    print(tree.postOrderTraversal())
    print(tree.preOderTraversal())
    tree.findMin()
    tree.findMax()


