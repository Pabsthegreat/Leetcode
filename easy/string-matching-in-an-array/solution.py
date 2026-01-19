"""
[Description]
String Matching in an Array
https://leetcode.com/problems/string-matching-in-an-array/

Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

 
Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

 
Constraints:

  1 <= words.length <= 100
  1 <= words[i].length <= 30
  words[i] contains only lowercase English letters.
  All the strings of words are unique.

[Metadata]
- Difficulty: Easy
- Topics: Array, String, String Matching
- Slug: string-matching-in-an-array
"""

// [Solution]
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = set()
        for i in words:
            for j in words:
                if i in j and i!=j:
                    l.add(i)

        return list(l)