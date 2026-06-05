"""
[Description]
Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

 
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 
Constraints:

  1 <= s.length <= 1000
  s consist of only digits and English letters.

[Metadata]
- Difficulty: Medium
- Topics: Two Pointers, String, Dynamic Programming
- Slug: longest-palindromic-substring
"""

// [Solution]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Transform string
        # Example: "abba" -> "^#a#b#b#a#$"
        t = "^#" + "#".join(s) + "#$"

        n = len(t)
        p = [0] * n #radius array

        center = 0
        right = 0 #boundary of the best palindrome found so far

        for i in range(1, n - 1):
            mirror = 2 * center - i #mirror of i across the center of the rightmost palindrome

            # If i is inside the current right boundary,
            # use mirror information to 
            if i < right:
                p[i] = min(right - i, p[mirror]) #the palindrome at i exceeds right or palindrome at i fits inside longest palindrome. the gurantee of what we know, thats why min. prevents recomputation

            # Try to expand palindrome centered at i
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            # If palindrome centered at i expands past right,
            # update center and right
            if i + p[i] > right:
                center = i
                right = i + p[i]

        # Find max palindrome radius
        max_side_len = max(p)
        center_index = p.index(max_side_len)

        # Convert transformed index back to original string index
        start = (center_index - max_side_len) // 2

        return s[start:start + max_side_len]


        # if not s:
        #     return ""

        # #augment the string
        # t = "^#" + "#".join(s) + "#$"
        # right = 0 #the rightmost boundary of the longest substring
        # center = 0 #center of the rightmost substring

        # for i in range(1, len(s)):
        #     mirror = 2*center-i

        #     if i < right: #lies within the rightmost subs
        #         p[i] = min(right-i, p[mirror]) #the best gurantee we can do
            
        #     #expand
        #     while (t[i + p[i] + 1)] == t[ i - p[i] - 1]: #current + gurantee + 1
        #         p[i] += 1
            
        #     if i + p[i] > right: #update if palindrome is exceeding current boundary
        #         center = i
        #         right = i+p[i]
        
        # max_len = max(p) #max length of palindrome on one side
        # center_index = p.index(max_len) #find which center index the max length belongs to 

        # start = (center_index - max_len) // 2
        # return s[start:start+max_len]

