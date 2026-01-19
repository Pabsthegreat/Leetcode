"""
[Description]
Ransom Note
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

 
Constraints:

  1 <= ransomNote.length, magazine.length <= 105
  ransomNote and magazine consist of lowercase English letters.

[Metadata]
- Difficulty: Easy
- Topics: Hash Table, String, Counting
- Slug: ransom-note
"""

// [Solution]
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for i in magazine:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for j in ransomNote:
            if j not in d:
                return False
            else:
                if d[j] == 0:
                    return False
                else:
                    d[j] -= 1
        return True
