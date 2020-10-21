import unittest
from LCA import findLCA, Node

class TestLCA(unittest.TestCase):

    def testLCA1(self):
     root = Node(1) 
     root.left = Node(2) 
     root.right = Node(3) 
     root.left.left = Node(4) 
     root.left.right = Node(5) 
     root.right.left = Node(6) 
     root.right.right = Node(7) 
     self.assertEqual(findLCA(root, 4, 5), 2)

    def testLCA2(self):
     root = Node(1) 
     root.left = Node(2) 
     root.right = Node(3) 
     root.left.left = Node(4) 
     root.left.right = Node(5) 
     root.right.left = Node(6) 
     root.right.right = Node(7) 
     self.assertEqual(findLCA(root, 4, 6), 1)

    def testLCA3(self):
     root = Node(1) 
     root.left = Node(2) 
     root.right = Node(3) 
     root.left.left = Node(4) 
     root.left.right = Node(5) 
     root.right.left = Node(6) 
     root.right.right = Node(7) 
     self.assertEqual(findLCA(root, 3, 4), 1)

    def testLCA4(self):
     root = Node(1) 
     root.left = Node(2) 
     root.right = Node(3) 
     root.left.left = Node(4) 
     root.left.right = Node(5) 
     root.right.left = Node(6) 
     root.right.right = Node(7) 
     self.assertEqual(findLCA(root, 2, 4), 2)


if __name__ == '__main__':
    unittest.main()

