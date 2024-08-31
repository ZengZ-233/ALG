"""
https://leetcode.cn/problems/time-based-key-value-store/?envType=study-plan-v2&envId=binary-search
"""
import collections
from bisect import bisect


class TimeMap:
    def __init__(self):
        self.ans = collections.defaultdict(list)
        self.time = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.ans[key], timestamp)  # 升序插入timestamp
        self.time[timestamp] = value
        """
        time:                    ans:
        {1: 'bar'}               defaultdict(<class 'list'>, {'foo': [1]})
        {1: 'bar'}               defaultdict(<class 'list'>, {'foo': [1]})
        {1: 'bar', 4: 'bar2'}    defaultdict(<class 'list'>, {'foo': [1, 4]})
        {1: 'bar', 4: 'bar2'}    defaultdict(<class 'list'>, {'foo': [1, 4]})
        """

    def get(self, key: str, timestamp: int) -> str:
        print(self.time)
        if key in self.ans and self.ans[key][0] <= timestamp:
            k = bisect.bisect(self.ans[key], timestamp)  # 二分查找timestamp的索引位置
            return self.time[self.ans[key][k - 1]]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

