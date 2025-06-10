class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        t = len(nums)//2
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] > t:
                    return i
            else:
                d[i] = 1
                if d[i] > t:
                    return i
# //O(n) time complexity
# //This solution uses a dictionary to count occurrences of each element.

# optimal: Moore's Voting Algorithm : Voting algorithm is an efficient way to find the majority element in linear time and constant space.
# Majority element always out votes the other elements, so we can keep track of a candidate and its count. When the count reaches zero, we switch to a new candidate.
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += 1 if num == candidate else -1

#         return candidate