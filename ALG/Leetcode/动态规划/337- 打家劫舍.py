"""
https://leetcode.cn/problems/house-robber-iii/description/?envType=study-plan-v2&envId=dynamic-programming
video讲解:https://www.bilibili.com/video/BV1vu4y1f7dn/?vd_source=37e31518cc82504f3880acfd557df9ef
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root) -> int:
        def dfs(node):
            if node is None:
                return 0,0
            l,l_not=dfs(node.left)
            r,r_not=dfs(node.right)
            rob=l_not+r_not+node.val
            not_rob=max(l,l_not)+max(r,r_not)
            return rob,not_rob
        return max(dfs(root))