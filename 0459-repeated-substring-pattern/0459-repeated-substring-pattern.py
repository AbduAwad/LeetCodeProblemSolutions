class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)//2+1):
            if s[:i] * (len(s)//i) == s:
                return True
        return False                                                                                                            