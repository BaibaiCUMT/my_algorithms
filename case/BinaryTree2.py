class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None


    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinartTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t


    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rigtChild


    def getLeftChild(self):
        return self.leftChild


    def setRootVal(self,obj):
        self.key = obj


    def getRootVal(self):
        return self.key
