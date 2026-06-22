"""
[Description]
Maximum Total Subarray Value II
https://leetcode.com/problems/maximum-total-subarray-value-ii/

You are given an integer array nums of length n and an integer k.

You must select exactly k distinct subarrays nums[l..r] of nums. Subarrays may overlap, but the exact same subarray (same l and r) cannot be chosen more than once.

The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).

The total value is the sum of the values of all chosen subarrays.

Return the maximum possible total value you can achieve.

 
Example 1:

Input: nums = [1,3,2], k = 2

Output: 4

Explanation:

One optimal approach is:

  Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
  Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.

Adding these gives 2 + 2 = 4.

Example 2:

Input: nums = [4,2,5,1], k = 3

Output: 12

Explanation:

One optimal approach is:

  Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4.
  Choose nums[1..3] = [2, 5, 1]. The maximum is 5 and the minimum is 1, so the value is also 4.
  Choose nums[2..3] = [5, 1]. The maximum is 5 and the minimum is 1, so the value is again 4.

Adding these gives 4 + 4 + 4 = 12.

 
Constraints:

  1 <= n == nums.length <= 5 * 10​​​​​​​4
  0 <= nums[i] <= 109
  1 <= k <= min(105, n * (n + 1) / 2)

[Metadata]
- Difficulty: Hard
- Topics: Array, Greedy, Segment Tree, Heap (Priority Queue)
- Slug: maximum-total-subarray-value-ii
"""

// [Solution]
from collections import deque

class Solution(object):
    def maxTotalValue(self, nums, k):
        n = len(nums)
        total_count = n * (n + 1) // 2

        def sum_all_ranges():
            # --- Sum of all subarray maximums via monotonic stack ---
            max_sum = 0
            stack = []
            for i in range(n + 1):
                # Sentinel value triggers flushing the remaining stack
                cur = float("inf") if i == n else nums[i]
                while stack and nums[stack[-1]] < cur:
                    j = stack.pop()
                    left = j - (stack[-1] if stack else -1)
                    right = i - j
                    max_sum += nums[j] * left * right
                stack.append(i)

            # --- Sum of all subarray minimums via monotonic stack ---
            min_sum = 0
            stack = []
            for i in range(n + 1):
                cur = float("-inf") if i == n else nums[i]
                while stack and nums[stack[-1]] > cur:
                    j = stack.pop()
                    left = j - (stack[-1] if stack else -1)
                    right = i - j
                    min_sum += nums[j] * left * right
                stack.append(i)

            return max_sum - min_sum

        total_sum = sum_all_ranges()

        def count_sum_ge(x):
            """
            Returns count and sum of subarray ranges that are >= x,
            using a two-pointer + compressed monotonic deque technique.
            """
            if x <= 0:
                return total_count, total_sum

            # Each deque stores (value, count) pairs, compressing equal-contribution
            # elements to avoid per-element front-shrink overhead.
            maxdq = deque()  # decreasing deque tracking running sum of maximums
            mindq = deque()  # increasing deque tracking running sum of minimums

            sum_max = 0  # sum of max(nums[left..right]) over all valid windows ending at right
            sum_min = 0  # sum of min(nums[left..right]) over all valid windows ending at right

            count_lt = 0  # count of subarrays with range < x
            sum_lt = 0    # sum of ranges of subarrays with range < x

            left = 0

            for right, val in enumerate(nums):
                # --- Extend right: merge into max deque ---
                cnt = 1
                while maxdq and maxdq[-1][0] <= val:
                    old_val, old_cnt = maxdq.pop()
                    sum_max -= old_val * old_cnt  # remove displaced max contributions
                    cnt += old_cnt
                maxdq.append([val, cnt])
                sum_max += val * cnt  # add new max contributions in bulk

                # --- Extend right: merge into min deque ---
                cnt = 1
                while mindq and mindq[-1][0] >= val:
                    old_val, old_cnt = mindq.pop()
                    sum_min -= old_val * old_cnt  # remove displaced min contributions
                    cnt += old_cnt
                mindq.append([val, cnt])
                sum_min += val * cnt  # add new min contributions in bulk

                # --- Shrink left: drop subarrays whose range >= x ---
                while maxdq[0][0] - mindq[0][0] >= x:
                    # Decrement the leftmost contribution by 1 window step
                    sum_max -= maxdq[0][0]
                    maxdq[0][1] -= 1
                    if maxdq[0][1] == 0:
                        maxdq.popleft()  # exhausted this compressed block

                    sum_min -= mindq[0][0]
                    mindq[0][1] -= 1
                    if mindq[0][1] == 0:
                        mindq.popleft()

                    left += 1

                # All subarrays nums[left..right] ... nums[right..right] have range < x
                valid_count = right - left + 1
                count_lt += valid_count
                sum_lt += sum_max - sum_min  # accumulated range sum for valid window

            return total_count - count_lt, total_sum - sum_lt

        # --- Binary search for the k-th largest range value (threshold) ---
        low = 0
        high = max(nums) - min(nums)

        while low < high:
            mid = (low + high + 1) // 2
            count, _ = count_sum_ge(mid)
            # Find largest threshold such that at least k subarrays have range >= threshold
            if count >= k:
                low = mid
            else:
                high = mid - 1

        threshold = low

        # --- Collect exact answer ---
        # Sum all ranges strictly above threshold, then pad remaining slots with threshold
        count_greater, sum_greater = count_sum_ge(threshold + 1)
        remaining = k - count_greater
        return sum_greater + remaining * threshold  # fill remaining k slots at threshold value