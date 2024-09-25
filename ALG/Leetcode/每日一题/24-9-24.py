"""
2207. 字符串中最多数目的子序列
https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/description/?envType=daily-question&envId=2024-09-24
"""

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        x, y = pattern
        print(x,",",y)
        ans = cnt_x = cnt_y = 0
        for c in text:
            if c == y:
                ans += cnt_x
                cnt_y += 1
            if c == x:
                cnt_x += 1
        return ans + max(cnt_x, cnt_y)