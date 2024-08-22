class Solution:
    def findComplement(self, num: int) -> int:
        binaryNum = str(bin(num)[2:])
        binLength = len(binaryNum)
        answer = 0
        for i in range(binLength - 1, -1, -1):
            if binaryNum[i] == '0':
                answer += (2**(binLength - i - 1))
        return answer