"""
[Description]
Shortest Word Distance II
https://leetcode.com/problems/shortest-word-distance-ii/

Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

  WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
  int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

 
Example 1:

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1

 
Constraints:

  1 <= wordsDict.length <= 3 * 104
  1 <= wordsDict[i].length <= 10
  wordsDict[i] consists of lowercase English letters.
  word1 and word2 are in wordsDict.
  word1 != word2
  At most 5000 calls will be made to shortest.

[Metadata]
- Difficulty: Medium
- Topics: Array, Hash Table, Two Pointers, String, Design
- Slug: shortest-word-distance-ii
"""

// [Solution]
class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.d = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.d:
                self.d[wordsDict[i]] = [i]
            else:
                self.d[wordsDict[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = self.d[word1]
        list2 = self.d[word2]
        
        i, j = 0, 0
        min_dist = float('inf')
        
        # Two pointer approach
        while i < len(list1) and j < len(list2):
            min_dist = min(min_dist, abs(list1[i] - list2[j]))
            
            # Move the pointer pointing to smaller index
            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        
        return min_dist