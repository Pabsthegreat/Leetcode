"""
[Description]
Fizz Buzz
https://leetcode.com/problems/fizz-buzz/

Given an integer n, return a string array answer (1-indexed) where:

  answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
  answer[i] == "Fizz" if i is divisible by 3.
  answer[i] == "Buzz" if i is divisible by 5.
  answer[i] == i (as a string) if none of the above conditions are true.

 
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]
Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

 
Constraints:

  1 <= n <= 104

[Metadata]
- Difficulty: Easy
- Topics: Math, String, Simulation
- Slug: fizz-buzz
"""

// [Solution]
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l =[]
        c = 1
        while c != n+1:
            s = str(c)
            thr = (c % 3 == 0)
            fiv = (c % 5 == 0)
            if fiv and thr is True:
                l += ["FizzBuzz"]
            elif thr == True and fiv == False:
                l += ["Fizz"]
            elif fiv == True and thr == False:
                l += ["Buzz"]
            else:
                l+=[s]
            c+=1

        return l

        