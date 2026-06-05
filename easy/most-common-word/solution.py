"""
[Description]
Most Common Word
https://leetcode.com/problems/most-common-word/

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Note that words can not contain punctuation symbols.

 
Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:

Input: paragraph = "a.", banned = []
Output: "a"

 
Constraints:

  1 <= paragraph.length <= 1000
  paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
  0 <= banned.length <= 100
  1 <= banned[i].length <= 10
  banned[i] consists of only lowercase English letters.

[Metadata]
- Difficulty: Easy
- Topics: Array, Hash Table, String, Counting
- Slug: most-common-word
"""

// [Solution]
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        d = {}
        w = ""
        for i in paragraph:
            if i.isalpha():
                w+=i.lower()
            elif w:
                if w in banned:
                    w = ""
                    continue
                elif w in d:
                    d[w]+=1
                    w=""
                else:
                    d[w] = 1
                    w = ""
            else:
                continue
        if w:
            if w in d:
                d[w]+=1
            else:
                d[w]=1
        else:
            pass
        return max(d, key=d.get)