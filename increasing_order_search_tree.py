class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def increasingBST(self, root: TreeNode) -> TreeNode:
#        pass
arr=[]
def inorder(root):
    if(root!=None):
        inorder(root.left)
        arr.append(root.val)
        inorder(root.right)

root=TreeNode(10)
root.left=TreeNode(11)
root.right=TreeNode(12)
root.left.left=TreeNode(13)
root.left.right=TreeNode(14)
# root.right.left=TreeNode(15)
# root.right.right=TreeNode(16)
inorder(root)
print(arr)