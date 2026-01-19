"""
[Description]
Find Words That Can Be Formed by Characters
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

 
Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

 
Constraints:

  1 <= words.length <= 1000
  1 <= words[i].length, chars.length <= 100
  words[i] and chars consist of lowercase English letters.

[Metadata]
- Difficulty: Easy
- Topics: Array, Hash Table, String, Counting
- Slug: find-words-that-can-be-formed-by-characters
"""

// [Solution]
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        d = {}
        s = set(chars)
        c=0
        for i in s:
            d[i]=chars.count(i)
        for j in words:
            r = set(j)
            if len(r) > len(s):
                continue
            else:
                f = True
                for i in r:
                    if (i in s) and (j.count(i) <= d[i]):
                        continue
                    else:
                        f = False
                        break
                if f == True:
                    c+= len(j)
        return c