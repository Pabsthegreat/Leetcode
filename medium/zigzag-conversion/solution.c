/*
[Description]
Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

 
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

 
Constraints:

  1 <= s.length <= 1000
  s consists of English letters (lower-case and upper-case), ',' and '.'.
  1 <= numRows <= 1000

[Metadata]
- Difficulty: Medium
- Topics: String
- Slug: zigzag-conversion
*/

// [Solution]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct node {
    char str[1000];
    struct node* next;
    struct node* prev;
};

char* convert(char* s, int numRows) {
    if (numRows == 1) return s; 

    struct node* head = NULL;
    struct node* pres = NULL;

    for (int i = 0; i < numRows; i++) {
        struct node* temp = (struct node*)malloc(sizeof(struct node));
        temp->next = NULL;
        temp->prev = pres;
        temp->str[0] = '\0'; 
        if (head == NULL) {
            head = temp;
        } else {
            pres->next = temp;
        }
        pres = temp;
    }

   
    pres = head;
    bool rev = false; 
    int j = 0;

    while (s[j] != '\0') {
        
        int len = strlen(pres->str);
        pres->str[len] = s[j];
        pres->str[len + 1] = '\0';

        if (pres->next == NULL) {
            rev = true;
        }
        if (pres->prev == NULL) {
            rev = false;
        }

        if (rev) {
            pres = pres->prev;
        } else {
            pres = pres->next;
        }

        j++;
    }

    // Collect the result from all rows (nodes)
    static char result[1000] = ""; // Static so we can return it
    result[0] = '\0'; // Initialize the result string to empty
    pres = head;

    while (pres != NULL) {
        strcat(result, pres->str);
        pres = pres->next;
    }
    return result;
}


