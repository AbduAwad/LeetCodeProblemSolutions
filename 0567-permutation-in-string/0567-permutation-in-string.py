class Solution(object):
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        left = 0
        right = len(s1) - 1
        mapS1, mapS2 = {}, {}
        for char in s1:
            mapS1[char] = mapS1.setdefault(char, 0) + 1

        x = len(s2) - len(s1) + 1
        for j in range(x):
            i = left
            while i < right + 1:
                mapS2[s2[i]] = mapS2.setdefault(s2[i], 0) + 1
                i += 1
            if (mapS1 == mapS2):
                return True
            mapS2 = {}
            left += 1
            right += 1
        return False
