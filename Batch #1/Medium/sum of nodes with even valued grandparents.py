"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

Example 1:
          6
       /     \
      7       8
     / \     /  \
    2   7   1    3
  /    / \        \
9     1   4         5

"""


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
            if not root:
                return 0
        
            stack = []
            stack.append((root,[root.val]))
            sums = 0
            
            while stack:
                node, fam = stack.pop()
                
                # check fam length and if grandparens are even
                if len(fam) > 2 and fam[-3]%2 == 0: 
                        sums+=node.val
                    
                # DFS while tracking granparents
                if node.left:
                    stack.append((node.left,fam+[node.left.val]))
                if node.right:
                    stack.append((node.right,fam+[node.right.val]))                
                    
            return sums