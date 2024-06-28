class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        numFound, i = 0,0
        for char in s:
            while i < (len(t)):
                if char == t[i]:
                    numFound += 1
                    i += 1
                    break
                i += 1
        return numFound == len(s)