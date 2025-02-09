# A Binary Tree Node 
class Node: 
    # Constructor
    def __init__(self, key): 
        self.key =  key 
        self.left = None
        self.right = None
  
# Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path  exists, otherwise returns false 
def findPath(root, path, k): 
  
    # Default Case 
    if root is None: 
        return False
  
    # Store this node in path vector. Node will be removed if not in path from root to k 
    path.append(root.key) 
  
    # See if the k is same as root's key 
    if root.key == k : 
        return True
  
    # Check if k is found in left or right sub-tree 
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 
  
    # If not present in subtree rooted with root, remove root from path and return false 
       
    path.pop() 
    return False
  
# Returns LCA if node n1 and n2 are present in the given Binary Tree, otherwise returns -1 
def findLCA(root, n1, n2): 
  
    # To store paths to n1 and n2 from the root 
    path1 = [] 
    path2 = [] 
  
    # Find paths from root to n1 and root to n2. 
    # If either n1 or n2 is not present, returns -1.  
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
        return -1 
  
    # Compare the paths to get the first different value 
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
  
print('LCA(3,7) = ' , findLCA(root, 3, 7))
print('LCA(4,6) = ' , findLCA(root, 4, 6))
print('LCA(2,5) = ' , findLCA(root, 2, 5))
print('LCA(1,2) = ' , findLCA(root, 1, 2))
