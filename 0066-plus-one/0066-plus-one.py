class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_str = ""
        for digit in digits:
            digit_str += str(digit)

        digit_int = int(digit_str) + 1
        new_digit_str = str((digit_int))

        new_digit_list = []
        for digit in new_digit_str:
            new_digit_list.append(int(digit))
            
        return new_digit_list