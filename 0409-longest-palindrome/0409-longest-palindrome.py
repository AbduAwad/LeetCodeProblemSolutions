class Solution:
    def longestPalindrome(self, s: str) -> int:

        letterCount = {}
        for char in s:
            letterCount[char] = letterCount.setdefault(char, 0) + 1
            
        count = 0
        for num in letterCount.values():
            if num % 2 == 0:
                count += num
            else: # add even number of the odd:
                count += num - 1

        if count < len(s):
            return count + 1        
        return count