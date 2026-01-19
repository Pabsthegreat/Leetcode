"""
[Description]
Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Every close bracket has a corresponding open bracket of the same type.

 
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 
Constraints:

  1 <= s.length <= 104
  s consists of parentheses only '()[]{}'.

[Metadata]
- Difficulty: Easy
- Topics: String, Stack
- Slug: valid-parentheses
"""

// [Solution]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:  # It's a closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:  # It's an opening bracket
                stack.append(char)
        return len(stack) == 0