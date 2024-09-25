"""
https://leetcode.cn/problems/binary-search/description/?envType=study-plan-v2&envId=binary-search
"""
from typing import List


# -------------非二分方法-----------------
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)

# -----------------二分方法-------------------
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            elif nums[m] > target: j = m - 1
            else: return m
        return -1
