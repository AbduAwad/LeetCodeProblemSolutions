class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = s.split()
        index = (len(str_list) - 1)
        final_word = str_list[index]
        
        return len(final_word)