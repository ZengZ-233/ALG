"""
https://leetcode.cn/problems/time-based-key-value-store/?envType=study-plan-v2&envId=binary-search
"""
from collections import defaultdict
import bisect


class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)
        self.value = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value[key].append(value)
        self.tm[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        if not self.tm[key]:
            return ""
        i = bisect.bisect_left(self.tm[key], timestamp)
        if 0<=i<len(self.tm[key]) and self.tm[key][i] == timestamp:
            return self.value[key][i]
        if 0<=i-1<len(self.tm[key]) and self.tm[key][i-1]<=timestamp:
            return self.value[key][i-1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
