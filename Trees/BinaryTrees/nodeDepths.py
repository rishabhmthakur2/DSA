"""
Question:
Write a function that takes in a Binary Tree and returns the sum of its node's depth.

"""

"""
Sample I/O:

Input:
tree =          1
        2               3
    4       5       6       7
  8   9

Output:
16
"""
def nodeDepths(root, depth = 0):
    # Write your code here.
    if root:
        return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
    else:
        return 0

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
TC: O(n)| SC: O(h) - recursion stack for the height of the tree

Explanation:

We iterate through the tree using recursion.
Starting from the root node which has a depth of 0, we add a depth of 1 to each next level/child and assign it to each node.
In the end, we keep a tally of number of children on each level using the depth and return the sum
"""