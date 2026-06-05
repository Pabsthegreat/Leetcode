"""
[Description]
Reverse Words in a String II
https://leetcode.com/problems/reverse-words-in-a-string-ii/

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

 
Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:
Input: s = ["a"]
Output: ["a"]

 
Constraints:

  1 <= s.length <= 105
  s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
  There is at least one word in s.
  s does not contain leading or trailing spaces.
  All the words in s are guaranteed to be separated by a single space.

[Metadata]
- Difficulty: Medium
- Topics: Two Pointers, String
- Slug: reverse-words-in-a-string-ii
"""

// [Solution]
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        s.reverse()
        b,e = 0,0
        def reverse(left,right):
            while left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -=1 

        while e<l-1:
            print(b,e)
            while s[e] != " " and e < l-1:
                e+=1
            if s[e] == ' ':
                reverse(b,e-1)
            else:
                reverse(b,e)
            e += 1
            b = e