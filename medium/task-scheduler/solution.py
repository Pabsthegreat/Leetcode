"""
[Description]
Task Scheduler
https://leetcode.com/problems/task-scheduler/

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 
Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 
Constraints:

  1 <= tasks.length <= 104
  tasks[i] is an uppercase English letter.
  0 <= n <= 100

[Metadata]
- Difficulty: Medium
- Topics: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
- Slug: task-scheduler
"""

// [Solution]
from collections import Counter
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        frequencies = Counter(tasks)

        heap = [-frequency for frequency in frequencies.values()]
        heapq.heapify(heap)

        time = 0

        while heap:
            used_tasks = []
            slots_used = 0

            # One cycle has at most n + 1 positions
            for _ in range(n + 1):
                if not heap:
                    break

                frequency = heapq.heappop(heap)
                frequency += 1  # one occurrence completed
                slots_used += 1

                if frequency < 0:
                    used_tasks.append(frequency)

            # Put tasks back only after the cycle ends
            for frequency in used_tasks:
                heapq.heappush(heap, frequency)

            if heap:
                # Remaining positions in this cycle are idle
                time += n + 1
            else:
                # No tasks remain, so don't add unnecessary idle slots
                time += slots_used

        return time