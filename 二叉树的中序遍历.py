"""
人一生不会踏进同一条河流
__author__ = 'marseille'
__date__ = '2021/1/13 15:46'
"""
class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        pass
from collections import deque
class Solution:
    def __init__(self):
        self.traversal = []
        self.stack = deque()
    def inorderTraversal(self, root):
        result, stack = [], [(root, False)]

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    result.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return result
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        WHITE, GRAY = 0, 1
        self.stack.append((WHITE,root))
        while(self.stack):
            color, node = self.stack.pop()
            if not node:
                continue
            if color == WHITE:
                self.stack.append((WHITE, node.right))
                self.stack.append((GRAY, node))
                self.stack.append((WHITE, node.left))
            else:
                self.traversal.append(node.val)
        return self.traversal

