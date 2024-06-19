class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for char in s:
            map[char] = map.setdefault(char, 0) + 1
        for i in range(len(s)):
            if map.get(s[i]) == 1:
                return i
        return -1