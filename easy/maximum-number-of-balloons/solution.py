"""
[Description]
Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 
Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

 
Constraints:

  1 <= text.length <= 104
  text consists of lower case English letters only.

 
Note: This question is the same as  2287: Rearrange Characters to Make Target String.

[Metadata]
- Difficulty: Easy
- Topics: Hash Table, String, Counting
- Slug: maximum-number-of-balloons
"""

// [Solution]
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        li = Counter(text)
        def check(ch,n):
            c = li.get(ch,0)
            if c < n:
                return False
            else:
                li[ch] -= n
                return True
        c = 0
        while True:
            b = check("b",1)
            a = check('a',1)
            l = check('l',2)
            o = check('o',2)
            n = check('n',1)
            if not (b and a and l and o and n):
                return c
            c += 1
        return c