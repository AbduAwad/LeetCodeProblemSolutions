class Solution(object):
    def searchMatrix(self, matrix, target):
        leftArr, rightArr = 0, len(matrix)-1
        while leftArr <= rightArr:
            arrIndex = leftArr + ((rightArr - leftArr) // 2)
            if matrix[arrIndex][0] > target:
                rightArr = arrIndex - 1
            elif matrix[arrIndex][0] < target:
                leftArr = arrIndex + 1
            else:
                return True
        if matrix[arrIndex][0] > target:
            arrIndex -= 1
        left, right = 0, len(matrix[arrIndex])-1
        while left <= right:
            index = left + ((right - left) // 2)
            if matrix[arrIndex][index] > target:
                right = index - 1
            elif matrix[arrIndex][index] < target:
                left = index + 1
            else:
                return True
        return False