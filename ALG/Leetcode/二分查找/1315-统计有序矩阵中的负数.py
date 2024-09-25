"""
https://leetcode.cn/problems/count-negative-numbers-in-a-sorted-matrix/description/?envType=study-plan-v2&envId=binary-search
"""
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for li in grid:
            l, r = 0, len(li)
            while l < r:
                mid = (l + r) // 2
                if li[mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            ans += len(li) - l
        return ans
