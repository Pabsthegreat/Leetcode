class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxLen = 0
        for i in range(0,len(s)):
            d = set()
            for j in range(i,len(s)):
                
                if s[j] not in d:
                    d.add(s[j])
                else:
                    break
            if len(d) > maxLen:
                maxLen = len(d)
        
        return maxLen
