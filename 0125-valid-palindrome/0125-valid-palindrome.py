class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for i in range(len(s)):
            if (s[i].isdigit() or s[i].isalnum()):
                newS += s[i].lower()
        return newS == newS[::-1]