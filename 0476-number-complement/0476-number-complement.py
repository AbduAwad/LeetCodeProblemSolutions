class Solution:
    def findComplement(self, num: int) -> int:
        binaryNum = str(bin(num)[2:])
        binLength = len(binaryNum)
        answer = 0
        for i in range(binLength):
            if (binaryNum[binLength - i - 1] == '0'):
                answer += 2**i
        return answer