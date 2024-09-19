"""
https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/description/
"""
from cmath import inf
from functools import cache
from typing import List

class Trie:
    """前缀树模板"""
    def __init__(self):
        self.children = dict()
        self.isEnd = False


    def insert(self, word: str) -> None:
        node = self
        for s in word:
            if s not in node.children:
                node.children[s] = Trie()
            node = node.children[s]
        node.isEnd = True
    
    def searchPrefix(self, prefix: str) -> 'Trie':
        node = self
        for s in prefix:
            if s not in node.children:
                return None
            node = node.children[s]
        return node


    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd


    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        @cache
        def dfs(start: int, end: int) -> int:
            if trie.searchPrefix(target[start: end + 1]):
                return 1
            res = inf
            node = trie
            for k in range(start, end + 1):
                # 从左往右遍历，这样可以直接移动node的位置
                # 不需要每次都重新遍历字典树判断前缀
                if target[k] not in node.children:
                    # 当前位置匹配不上，最长可能前缀遍历完成，直接返回res
                    return res if res < inf else -1
                n1 = dfs(k + 1, end)
                if n1 != -1:
                    # 找到合法方案，更新最小值
                    res = min(res, n1 + 1)
                node = node.children[target[k]]  # 直接向后移动node指针
        
        return dfs(0, len(target) - 1)

