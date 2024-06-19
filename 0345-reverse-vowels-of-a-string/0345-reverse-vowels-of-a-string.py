class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelSet = set(['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O','U'])
        start = 0
        end = len(s) - 1
        s = list(s)
        while start < end:
            if (s[start] in vowelSet and s[end] in vowelSet):
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                start += 1
                end -= 1
            if (s[start] not in vowelSet):
                start += 1
            if (s[end] not in vowelSet):
                end -= 1

        output = ""
        for char in s:
            output += char
        return output
        
            

