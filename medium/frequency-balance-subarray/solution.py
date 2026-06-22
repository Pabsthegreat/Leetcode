"""
[Description]
Frequency Balance Subarray
https://leetcode.com/problems/frequency-balance-subarray/

You are given an integer array ​​​​​​​nums.

Define a frequency balance subarray as follows:

  If the subarray contains only one distinct value, it is frequency balanced.
  Otherwise, there must exist a positive integer f such that every distinct value in the subarray occurs either f or 2 * f times, and both frequencies occur among the distinct values.

Return an integer denoting the length of the longest frequency balance subarray.

 
Example 1:

Input: nums = [1,2,2,1,2,3,3,3]

Output: 5

Explanation:

  The longest frequency balance subarray is [2, 1, 2, 3, 3].
  The elements that appear most frequently are 2 and 3, both appearing twice.
  The remaining element 1 appears once, meeting the requirements.

Example 2:

Input: nums = [5,5,5,5]

Output: 4

Explanation:

  The longest frequency balance subarray is [5, 5, 5, 5].
  The element that appears most frequently is 5.
  There are no other elements meeting the requirements.

Example 3:

Input: nums = [1,2,3,4]

Output: 1

Explanation:

Since all elements appear only once, the length of the longest frequency balance subarray is 1.

 
Constraints:

  1 <= nums.length <= 10​​​​​​​3
  1 <= nums[i] <= 10​​​​​​​9

[Metadata]
- Difficulty: Medium
- Topics: 
- Slug: frequency-balance-subarray
"""

// [Solution]
class Solution:
    def getLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            freq = defaultdict(int)
            cnt = defaultdict(int)
            for j in range(i,len(nums)):
                n = nums[j]
                old_freq = cnt[n]
                if old_freq > 0:
                    freq[old_freq] -= 1
                    if freq[old_freq] == 0:
                        del freq[old_freq]
                new_freq = cnt[n]+1
                cnt[n] = new_freq
                freq[new_freq] += 1
                length = j-i+1
                b = self.balance(cnt,freq)
                if b:
                    ans = max(length,ans)
        return ans

    def balance(self,cnt,freq):
        if len(cnt) == 1:
            return True
        if len(freq) != 2:
            return False
        x,y = list(freq.keys())
        ma = max(x,y)
        mi = min(x,y)
        return ma == mi*2
        