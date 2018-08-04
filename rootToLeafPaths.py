# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        totlist = []
        self.RootToLeafSum(A,B,[],totlist)
        return totlist
        
    def RootToLeafSum(self, A, B, path, totlist):
        if not A:
            return
                
        path.append(A.val)
        B -= A.val
        if B == 0 and A.left is None and A.right is None:
            totlist.append(path[:])
            return

        if A.left:
            self.RootToLeafSum(A.left, B, path[:], totlist)
        if A.right:
            self.RootToLeafSum(A.right, B, path[:], totlist)    

