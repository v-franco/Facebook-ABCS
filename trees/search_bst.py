class Node:
    def __init__(self, val, left = None, right = None):
        self.value = val;
        self.left = left;
        self.right = right;

    
def contains(rootNode, searchValue):
    if not rootNode:
        return False
    
    if rootNode.value == searchValue:
        return True
    
    if rootNode.value > searchValue:
        return contains(rootNode.left, searchValue)
    else:
        return contains(rootNode.right, searchValue)
    
    
root = Node(15, Node(11), Node(22, Node(13), Node(25)))
print(contains(root, 11))