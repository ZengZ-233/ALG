"""
https://leetcode.cn/problems/maximum-multiplication-score/description/
解题:https://www.bilibili.com/video/BV1Qp4me2Emz/?vd_source=37e31518cc82504f3880acfd557df9ef
"""
from cmath import inf
from functools import cache
from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @cache
        def dfs(i,j):
            if j<0:
                return 0
            if i<0:
                return -inf
            return max(dfs(i-1,j),dfs(i-1,j-1)+a[j]*b[i])
        
        ans=dfs(len(b)-1,3)
        dfs.cache_clear()
        return ans