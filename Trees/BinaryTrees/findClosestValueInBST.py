"""
Question:

Write a function that takes in a Binary Search Tree (BST) and a target integer value and 
returns the closest value to that target value contained in the BST. You can assume that 
there will only be one closest value.
"""

"""
Sample I/O:

Input:
          10
      5       15
    2   5  13   22
1           14

target = 12

Output:
13
"""

def helper(currentTarget, possibleTarget, target):
    if abs(currentTarget - target) > abs(possibleTarget - target):
        return possibleTarget
    else:
        return currentTarget

def findClosestValueInBst(tree, target):
    # Write your code here.
    offset = float('inf')
    closestTarget = tree.value
    while tree:
        if tree.value < target:
            tree = tree.right
        elif tree.value > target:
            tree = tree.left
        else:
            return target
        if(tree is not None):
            closestTarget = helper(closestTarget, tree.value, target)
    return closestTarget

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""
TC: O(logn)| SC: O(1)

Explanation:
- The key is to divide the tree in half at each iteration/step by using the unique nature of BSTs.
- We start by placing the closest node to be the root node and the distance of the chosen target (root)
with the required target to be infinity.
- If our target is greater than the current target, we go to the elements on the right, else we go left
- At each step, we compare the distance of the new traversal root and the required target
    vs the current;y selected node and required target.
- In case the absolute distance of this node is lesser, we place this node to be the closest node
- In the end, we return the closest node.
"""