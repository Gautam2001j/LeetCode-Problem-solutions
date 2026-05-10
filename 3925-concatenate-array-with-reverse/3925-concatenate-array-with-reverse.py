class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = nums[::-1]
        res = []
        for i in nums:
            res.append(i)
        for i in temp:
            res.append(i)
        return res