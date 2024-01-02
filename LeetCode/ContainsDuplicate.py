class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        frequencies = {i: nums.count(i) for i in set(nums)}
        return any([frequencies[i] > 1 for i in frequencies])

