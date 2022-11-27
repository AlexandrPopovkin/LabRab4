"""class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def showing(self):
        if self.left:
            self.left.showing()
        print(self.data),
        if self.right:
            self.right.showing()

    def insert_string(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_string(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_string(data)

        else:
            self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add_string(self, data):
        if self.root == None:
            self.root = Node(data)



root = Node(10)
root.insert_string(6)
root.insert_string(14)
root.insert_string(3)
root.showing()"""

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
class Tree:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None
    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)
    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)
#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(tree.find(3).v)
print(tree.find(10))
tree.deleteTree()