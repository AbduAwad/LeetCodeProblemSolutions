class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for x in range(0, 9): #rows
            num_set1 = set()
            num_set2 = set()
            count_nums1 = 0
            count_nums2 = 0
            for y in range(0,9): 
                
                if self.isConvertibleToInt(board[x][y]):
                    count_nums1 +=1
                    num_set1.add(board[x][y])
                if len(num_set1) != count_nums1:
                    return False

                if self.isConvertibleToInt(board[y][x]): 
                    count_nums2 +=1
                    num_set2.add(board[y][x])
                if len(num_set2) != count_nums2:
                    return False

        for i in range(0, 9, 3): 
            for j in range(0, 9, 3): 
                num_set = set()
                count_nums = 0
                for x in range(i, i + 3):  
                    for y in range(j, j + 3): 
                        if self.isConvertibleToInt(board[x][y]):
                            count_nums += 1
                            num_set.add(board[x][y])
                        if len(num_set) != count_nums:
                            return False
        return True

    def isConvertibleToInt(self, s):
        try:
            int(s) 
            return True 
        except ValueError:
            return False 
