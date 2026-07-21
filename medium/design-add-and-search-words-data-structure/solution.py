"""
[Description]
Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

  WordDictionary() Initializes the object.
  void addWord(word) Adds word to the data structure, it can be matched later.
  bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 
Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

 
Constraints:

  1 <= word.length <= 25
  word in addWord consists of lowercase English letters.
  word in search consist of '.' or lowercase English letters.
  There will be at most 2 dots in word for search queries.
  At most 104 calls will be made to addWord and search.

[Metadata]
- Difficulty: Medium
- Topics: String, Depth-First Search, Design, Trie
- Slug: design-add-and-search-words-data-structure
"""

// [Solution]
class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = {}


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.isWord = True

    def search(self, word):
        def dfs(index, node):
            if index == len(word):
                return node.isWord

            ch = word[index]

            if ch == ".":
                for child_node in node.children.values():
                    if dfs(index + 1, child_node):
                        return True
                return False

            else:
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)