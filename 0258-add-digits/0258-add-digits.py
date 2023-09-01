class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        for char in str(num):
            sum += int(char)
        if sum < 10:
            return sum
        return self.addDigits(sum)