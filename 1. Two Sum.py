class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target):
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                return [i, nums.index(target-nums[i], i+1)]

    def twoSum3(self, nums, target):
        """425ms"""
        m = []
        for i in range(len(nums)):
            if target-nums[i] in m:
                return [nums.index(target-nums[i]), i]
            m.append(nums[i])

    def twoSum4(self, nums, target):
        """554ms"""
        for i in range(len(nums)):
            if target-nums[i] in nums[:i]:
                return [nums.index(target-nums[i]), i]

    def twoSum5(self, nums, target):
        """455ms"""
        m = []
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in m:
                return [nums.index(complement), i]
            m.append(nums[i])
