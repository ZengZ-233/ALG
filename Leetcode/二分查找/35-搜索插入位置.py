"""
https://leetcode.cn/problems/search-insert-position/description/?envType=study-plan-v2&envId=binary-search
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a,b=0,len(nums)-1
        while a<=b:
            c=(a+b)//2
            if nums[c]<target:
                a=c+1
            elif nums[c]>target:
                b=c-1
            else:
                return c
        return a