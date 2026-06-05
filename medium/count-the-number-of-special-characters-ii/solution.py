"""
[Description]
Count the Number of Special Characters II
https://leetcode.com/problems/count-the-number-of-special-characters-ii/

You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

 
Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.

 
Constraints:

  1 <= word.length <= 2 * 105
  word consists of only lowercase and uppercase English letters.

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, String
- Slug: count-the-number-of-special-characters-ii
"""

// [Solution]
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            lower = ch
            upper = ch.upper()

            # both must exist
            if lower in word and upper in word:

                # last lowercase occurrence
                last_lower = word.rfind(lower)

                # first uppercase occurrence
                first_upper = word.find(upper)

                if last_lower < first_upper:
                    res += 1

        return res