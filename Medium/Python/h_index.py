class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h
    
# Time Complexity: O(n log n) due to sorting, where n is the number of citations.
#h index is the maximum value h such that the given author has published at least h papers that have each been cited at least h times.
#checking from the highest citation count downwards, we can determine the h-index by counting how many papers meet the criteria.