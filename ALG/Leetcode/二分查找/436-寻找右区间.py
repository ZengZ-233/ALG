"""
https://leetcode.cn/problems/find-right-interval/description/?envType=study-plan-v2&envId=binary-search
"""
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        x = {intervals[i][0]: i for i in range(len(intervals))}
        starts = sorted([i[0] for i in intervals])
        ans = [-1] * len(intervals)
        for i in range(len(intervals)):
            target = intervals[i][1]
            left, right = 0, len(intervals) - 1
            while left < right:
                mid = (left + right) // 2
                if starts[mid] >= target:
                    ans[i] = x[starts[mid]]
                    right = mid
                elif starts[mid] < target:
                    left = mid + 1
            if starts[left] >= target:
                ans[i] = x[starts[left]]
        return ans
