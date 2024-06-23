class Solution(object):
    def countGoodSubstrings(self, s):
        left = 0
        right = 2
        count = 0
        while right < len(s):
            if (s[left] != s[left+1] and s[left+1] != s[right] and s[left] != s[right]):
                count += 1
            left += 1
            right += 1
        return count
