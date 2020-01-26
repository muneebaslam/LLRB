# 1 / True represents RED
# 0 / False represents BLACK


class Node:
    def __init__(self, value):
        self.value = value
        self.color = 1
        self.left = None
        self.right = None
    
class LLRB:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)
        self.root.color = 0
    
    def _insert(self, root, data):
        if not root:
            return Node(data)
        if data == root.value:
            return
        if data < root.value:
            root.left = self._insert(root.left, data)
        elif data > root.value:
            root.right = self._insert(root.right, data)
        
        if root.right and root.right.color:
            root = self.rotateLeft(root)
        if root.left and root.left.color and root.left.left and root.left.left.color:
            root = self.rotateRight(root)
        if root.right and root.right.color and root.left and root.left.color:
            root = self.colorFlip(root)  
        return root
    
    def rotateLeft(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        temp.color = node.color
        node.color = 1
        return temp
    
    def rotateRight(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        temp.color = node.color
        node.color = 1
        return temp
    
    def colorFlip(self, node):
        node.color = not(node.color)
        node.left.color = not(node.left.color)
        node.right.color = not(node.right.color)
        return node
    
    def delete(self,data):
        self.root = self._delete(self.root, data)
        self.root.color = 0
    
    def successor(self, node):
        if not node.left:
            return node
        return successor(node.left)
    
    def predecessor(self, node):
        if not node.right:
            return node
        return self.predecessor(node.right)
    
    def _delete(self, root, data):
        if not root:
            return None
        if root.value == data:
            if root == self.root:
                return None
            elif not root.left and not root.right:
                return None
            elif root.right:
                temp = self.successor(root.right)
                root.value = temp.value
                root.right = self._delete(root.right,temp.value)
            elif root.left:
                temp = self.predecessor(root.left)
                root.value = temp.value
                root.left = self._delete(root.left, temp.value)
        elif root.value > data and root.left:
            if root.left.color or root.left.left.color:
                root.left = self._delete(root.left, data)
            else:
                root = self.colorFlip(root)
                if root.right and root.right.left and root.right.left.color:
                    root.right = self.rotateRight(root.right)
                    root = self.rotateLeft(root)
                    root = self.colorFlip(root)
                root.left = self._delete(root.left, data)
        elif root.right:
            if root.left and root.left.color:
                root = self.rotateRight(root)
                root.right = self._delete(root.right, data)
            elif (root.right and root.right.color) or (root.right.left and root.right.left.color):
                root.right = self._delete(root.right, data)
            else:
                print(root.value)
                print(root.left.value)
                root = self.colorFlip(root)
                if root.left and root.left.left and root.left.left.color:
                    root = self.rotateRight(root)
                    print(root.value)
                    root = self.colorFlip(root)
                root.right = self._delete(root.right, data)
                
        if root.right and root.right.color:
            root = self.rotateLeft(root)
            
        if root.left and root.left.color and root.left.left and root.left.left.color:
            root = self.rotateRight(root)
            
        if root.right and root.right.color and root.left and root.left.color:
            root = self.colorFlip(root)
            
        return root
    
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, root, value):
        if not root:
            return False
        if root.value == value:
            return True
        elif value > root.value:
            return self._search(root.right, value)
        else:
            return self._search(root.left, value)
    
            






