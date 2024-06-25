class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left, right, count, maxCount = 0, 0, 0, 0
        currSubstring = set()
        while right < len(s):
            if (s[right] in currSubstring):
                while (s[right] in currSubstring):
                    currSubstring.remove(s[left])
                    left += 1
                    count -= 1
            currSubstring.add(s[right])
            count += 1
            right += 1
            maxCount = max(maxCount, count)
        return max(count, maxCount)
