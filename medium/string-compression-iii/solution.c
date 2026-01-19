/*
[Description]
String Compression III
https://leetcode.com/problems/string-compression-iii/

Given a string word, compress it using the following algorithm:

  Begin with an empty string comp. While word is not empty, use the following operation:

  
    Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
    Append the length of the prefix followed by c to comp.
  
  

Return the string comp.

 
Example 1:

Input: word = "abcde"

Output: "1a1b1c1d1e"

Explanation:

Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.

For each prefix, append "1" followed by the character to comp.

Example 2:

Input: word = "aaaaaaaaaaaaaabb"

Output: "9a5a2b"

Explanation:

Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.

  For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
  For prefix "aaaaa", append "5" followed by "a" to comp.
  For prefix "bb", append "2" followed by "b" to comp.

 
Constraints:

  1 <= word.length <= 2 * 105
  word consists only of lowercase English letters.

[Metadata]
- Difficulty: Medium
- Topics: String
- Slug: string-compression-iii
*/

// [Solution]

char* compressedString(char* word) {
    int len = strlen(word);
    char* c = (char *)malloc((2*len+1));
    int ind = 0;
    c[0]='\0';
    int count = 0;
    char cur = word[0];

    for(int i=0;i<len;i++){

        if(word[i]==cur && count<9){
            count++;
        }
        else{
            c[ind++]=count+'0';
            c[ind++]=cur;
            count = 1;
            cur = word[i];
        }
        
        
    }
    c[ind++]=count+'0';
    c[ind++]=cur;
    c[ind++]='\0';
    return c;
}
