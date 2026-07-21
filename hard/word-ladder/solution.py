"""
[Description]
Word Ladder
https://leetcode.com/problems/word-ladder/

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

  Every adjacent pair of words differs by a single letter.
  Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
  sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 
Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

 
Constraints:

  1 <= beginWord.length <= 10
  endWord.length == beginWord.length
  1 <= wordList.length <= 5000
  wordList[i].length == beginWord.length
  beginWord, endWord, and wordList[i] consist of lowercase English letters.
  beginWord != endWord
  All the words in wordList are unique.

[Metadata]
- Difficulty: Hard
- Topics: Hash Table, String, Breadth-First Search
- Slug: word-ladder
"""

// [Solution]
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        w = set(wordList)

        if endWord not in w:
            return 0

        q = deque()
        q.append((beginWord, 1))

        seen = set()
        seen.add(beginWord)

        letters = "abcdefghijklmnopqrstuvwxyz"
        l = len(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(l):
                word_list = list(word)
                original = word_list[i]

                for ch in letters:
                    if ch == original:
                        continue

                    word_list[i] = ch
                    new_word = "".join(word_list)

                    if new_word in w and new_word not in seen:
                        seen.add(new_word)
                        q.append((new_word, steps + 1))

        return 0