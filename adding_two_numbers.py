class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_copy = nums
        
        for i in range(len(nums_copy)):
            for j in range(len(nums_copy)):
                if(i != j and (nums_copy[i] + nums_copy[j] == target)):
                    return [i, j]
                
        