"""
[Description]
String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

  Whitespace: Ignore any leading whitespace (" ").
  Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
  Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
  Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.

 
Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^

Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^

Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^

Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^

Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.

 
Constraints:

  0 <= s.length <= 200
  s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

[Metadata]
- Difficulty: Medium
- Topics: String
- Slug: string-to-integer-atoi
"""

// [Solution]
class Solution:
    def myAtoi(self, s: str) -> int:
        #from here
        # s = s.strip()
        # if not s:
        #     return 0
        # sign = 1
        # r = "0"
        # if not (s[0].isdigit() or (s[0] in "+-")):
        #     return 0
        # if s[0] == "-":
        #     sign = -1
        # elif s[0] == "+":
        #     sign = 1
        # else:
        #     r += s[0]
        # if len(s) >= 2:
        #     i = 1 
        # else:
        #     return int(r)
        # while (i < len(s) and s[i].isdigit() and s[i] == "0"):
        #     i+=1
        # while i < len(s):
        #     if not s[i].isdigit():
        #         return int(r)* sign
        #     else:
        #         r += s[i]
        #     i+=1

        s = s.strip()
        if not s:
            return 0
        r = "0"
        sign = 0
        start = 0
        for i in s:
            if i.isdigit():
                if sign == 0:
                    sign = 1
                if start == 0 and i == "0":
                    continue
                elif start == 0 and i!="0":
                    start = 1
                    r+=i
                else:
                    r+=i
            elif i in "+-":
                if sign!= 0:
                    break
                elif i == "+":
                    sign = 1
                else:
                    sign = -1
            else:
                break

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        result = int(r) * sign if r else 0
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result


            