"""
Testing for P28, assumes file is named p28.py and imports as module:
"""
from p28 import insert


# Definition for a binary tree node.
"""
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
"""




def inorder(root):
  """
  Writes out the left subtree, root, right subtree.

  A quick helper function that does (in order) traversal function to see the trees 
  that are being built correctly.  See Section 6.8 for more on printing trees.
    
  :type root: TreeNode
  :rtype: str
  """
  
  if root == None:
    return ""
  return("("+inorder(root.left)+") <- "+str(root.val)+" -> ("+inorder(root.right)+")")


my_tree = None
my_tree = insert(my_tree, 10)
print("added first node")
print(inorder(my_tree))
#Some more values:
some_vals = [3,5,20,15,1]
for val in some_vals:
    my_tree = insert(my_tree, val)
    print(inorder(my_tree))

#Making another tree from [1,2,4,8,16,32]
double_vals = [1,2,4,8,16,32]
another_tree = None
for val in double_vals:
    another_tree = insert(another_tree, val)
    print(inorder(another_tree))
