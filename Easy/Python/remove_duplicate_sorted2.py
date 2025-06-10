class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        b = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] and b < 1:
                b += 1
                nums[k] = nums[i]
                k += 1
            elif nums[i] != nums[i-1]:
                b = 0
                nums[k] = nums[i]
                k += 1
        return k
# //O(n) time complexity
# //This solution allows for one duplicate of each element in the sorted array.

# optimal:
#  k = 2  # Points to the position to insert the next unique element

#         for i in range(2, len(nums)):
#             if nums[i] != nums[k - 2]:
#                 nums[k] = nums[i]
#                 k += 1
#         return k