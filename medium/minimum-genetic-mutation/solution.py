"""
[Description]
Minimum Genetic Mutation
https://leetcode.com/problems/minimum-genetic-mutation/

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

  For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 
Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

 
Constraints:

  0 <= bank.length <= 10
  startGene.length == endGene.length == bank[i].length == 8
  startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, String, Breadth-First Search
- Slug: minimum-genetic-mutation
"""

// [Solution]
from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)

        if endGene not in bank_set:
            return -1

        def one_diff(a, b):
            diff = 0
            for i in range(8):
                if a[i] != b[i]:
                    diff += 1
            return diff == 1

        q = deque([(startGene, 0)])
        visited = set([startGene])

        while q:
            gene, steps = q.popleft()

            if gene == endGene:
                return steps

            for next_gene in bank:
                if next_gene not in visited and one_diff(gene, next_gene):
                    visited.add(next_gene)
                    q.append((next_gene, steps + 1))

        return -1