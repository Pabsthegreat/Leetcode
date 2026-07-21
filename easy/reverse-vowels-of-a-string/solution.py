"""
[Description]
Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 
Constraints:

  1 <= s.length <= 3 * 105
  s consist of printable ASCII characters.

[Metadata]
- Difficulty: Easy
- Topics: Two Pointers, String
- Slug: reverse-vowels-of-a-string
"""

// [Solution]
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l,r = 0,len(s)-1
        while l < r:
            while l < len(s) and s[l] not in 'aeiouAEIOU':
                l+=1
            while r >= 0 and s[r] not in 'aeiouAEIOU':
                r -= 1
            if l < r:
                s[r],s[l] = s[l],s[r]
                l+=1
                r-=1
        return ''.join(s)