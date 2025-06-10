# 2. Cyclic Replacements — O(n) Time, O(1) Space
# This method moves each element to its correct rotated position, one cycle at a time:
#start is there to keep track of the starting index of the cycle, current is used to traverse through the cycle, and prev holds the value that will be moved to the next position.
#multiple cycles required if k and n are not coprime, which means that some elements will be moved multiple times until all elements are in their correct positions.
#number of cycles is determined by the greatest common divisor (gcd) of n and k, but in this case, we are not explicitly calculating gcd; instead, we are using a while loop to ensure all elements are moved.
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        count = 0  # To keep track of number of elements moved
        start = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if start == current:
                    break
            start += 1

# 1. Using Extra Space (Slicing) — O(n) Time, O(n) Space
# This method is simple and readable but uses extra space:

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

# 3. Reversal Algorithm — O(n) Time, O(1) Space
# This method reverses parts of the array to achieve the rotation in-place:

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k is greater than the array length

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining elements
        reverse(k, n - 1)