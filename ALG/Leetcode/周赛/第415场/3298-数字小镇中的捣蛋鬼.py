"""
https://leetcode.cn/problems/the-two-sneaky-numbers-of-digitville/description/
"""
from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        l,r=0,1
        res=[]
        while l<r and r<=len(nums)-1:
            if nums[l]==nums[r]:
                res.append(nums[l])
            l+=1
            r+=1
        return res
