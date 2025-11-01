class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        c = 0
        for i in range(l):
            if nums[i] == val:
                nums[i] = -1
                c +=1
        j = 0
        k = l-1
        while j < l-1 and k > l-c:
            if nums[j] == -1:
                while nums[k] == -1 and k > l-c:
                    k -= 1
                temp = nums[k]
                nums[k] = -1
                nums[j] = temp
            j += 1
        return l-c

# //remove in place , can use pop() as well.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Position to insert the next valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
# //O(n) time complexity
# two pointer approach most optimal for replacement or deletion in place.