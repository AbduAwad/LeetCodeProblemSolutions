class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        str_num = str(n)
        num_list = [int(i) for i in str_num]

        while True:
            new_num = 0
            for num in num_list:
                new_num += num**2

            if len(num_list) == 1:
                if num_list[0] == 1 or num_list[0] == 7:
                    return True
                else:
                    return False
                
            if new_num == 1:
                return True
            else:
                str_num = str(new_num)
                num_list = [int(i) for i in str_num]

            
