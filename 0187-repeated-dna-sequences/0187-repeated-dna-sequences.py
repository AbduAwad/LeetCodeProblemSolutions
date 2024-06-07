class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if (len(s) < 10):
            return []
            
        strs, output = set(), set()
        currString = s[0:10:]
        strs.add(currString)
        count = 10
        while count < len(s):
            currString = currString[1::]
            currString += s[count]
            if currString in strs:
                output.add(currString)
            strs.add(currString)
            count += 1
        return output