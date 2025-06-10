class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False  # We can't reach this point
            max_reach = max(max_reach, i + nums[i])
        return True
#greedy approach: we keep track of the maximum index we can reach at each step. If at any point the current index exceeds this maximum reach, we return False. If we can traverse the entire array without exceeding the maximum reach, we return True.
# Time Complexity: O(n), where n is the length of the input list nums.