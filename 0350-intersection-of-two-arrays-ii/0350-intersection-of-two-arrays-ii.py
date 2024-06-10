class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1, dict2 = {}, {}
        for num in nums1:
            dict1[num] = dict1.setdefault(num, 0) + 1
        for num in nums2:
            dict2[num] = dict2.setdefault(num, 0) + 1

        output = []
        if len(nums1) > len(nums2):
            for num in nums2:
                if (num in dict1):
                    output.append(num)
                    dict1[num] -= 1
                    dict2[num] -= 1
                    if (dict1[num] == 0) or (dict2[num] == 0):
                        dict1.pop(num)
                        dict2.pop(num)
        else:
            for num in nums1:
                if (num in dict2):
                    output.append(num)
                    dict1[num] -= 1
                    dict2[num] -= 1
                    if (dict1[num] == 0) or (dict2[num] == 0):
                        dict1.pop(num)
                        dict2.pop(num)
        return output