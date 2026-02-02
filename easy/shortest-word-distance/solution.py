"""
[Description]
Shortest Word Distance
https://leetcode.com/problems/shortest-word-distance/

Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 
Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

 
Constraints:

  2 <= wordsDict.length <= 3 * 104
  1 <= wordsDict[i].length <= 10
  wordsDict[i] consists of lowercase English letters.
  word1 and word2 are in wordsDict.
  word1 != word2

[Metadata]
- Difficulty: Easy
- Topics: Array, String
- Slug: shortest-word-distance
"""

// [Solution]
class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = -1
        w2 = -1
        d = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1 = i
                if w2 != -1:
                    d = min(d,abs(w1-w2))
            elif wordsDict[i] == word2:
                w2 = i
                if w1!= -1:
                    d = min(d,abs(w1-w2))
        return d