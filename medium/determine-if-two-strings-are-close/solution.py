"""
[Description]
Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/

Two strings are considered close if you can attain one from the other using the following operations:

  Operation 1: Swap any two existing characters.

  
    For example, abcde -> aecdb
  
  
  Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
  
    For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
  
  

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 
Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

 
Constraints:

  1 <= word1.length, word2.length <= 105
  word1 and word2 contain only lowercase English letters.

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, String, Sorting, Counting
- Slug: determine-if-two-strings-are-close
"""

// [Solution]
from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        # Both words must contain exactly the same characters
        if set(c1.keys()) != set(c2.keys()):
            return False

        # Their frequency distributions must match
        return sorted(c1.values()) == sorted(c2.values())