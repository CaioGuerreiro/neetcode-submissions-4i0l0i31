# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        queue = deque([root])

        while queue:
            new_level= []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                new_level.append(node.val)
                

                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            
            res.append(new_level[-1])
        return res
        