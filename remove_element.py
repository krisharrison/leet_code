"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

 

Constraints:

    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

"""
nums = [0,1,2,2,3,0,4,2]
nums2 = [1,2,3,4]
nums3 = [2,2,2,2]

class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        if nums == []:
            k = 0
            return k
        if len(nums) == 1:
            if nums[0] != val:
                k = 1
            elif nums[0] == val:
                k = 0
            return k
        
        #If all elements are the same
        counter = 0
        for num in nums:
            if num != val:
                counter = counter + 1

        #Initialize K
        if counter == len(nums):
            k = counter
            return k

        k = 0
        end = len(nums)-1

        #If not all elements are the same
        while k != end:
            print("K: ", k)
            if nums[k] != val:
                k = k+1
            elif nums[end] == val or (nums[k] == val and nums[end] == val):
                end = end-1

            if nums[k] == val:
                temp = nums[k]
                nums[k] = nums[end]
                nums[end] = temp

        return k


solution = Solution()
k = solution.removeElement(nums3,3)
print("K: ", k)
