"""
[Description]
Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""​​​​​​​

 
Constraints:

  1 <= str1.length, str2.length <= 1000
  str1 and str2 consist of English uppercase letters.

[Metadata]
- Difficulty: Easy
- Topics: Math, String
- Slug: greatest-common-divisor-of-strings
"""

// [Solution]
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter = str1 if len(str1) <= len(str2) else str2

        for length in range(len(shorter), 0, -1):
            candidate = shorter[:length]

            if len(str1) % length != 0 or len(str2) % length != 0:
                continue

            if (
                candidate * (len(str1) // length) == str1
                and candidate * (len(str2) // length) == str2
            ):
                return candidate

        return ""