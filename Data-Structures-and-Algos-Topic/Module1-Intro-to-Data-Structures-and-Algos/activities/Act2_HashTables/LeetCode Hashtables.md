### Interview Question for Hashtables ###

Prompt: Given a string, find the length of the longest substring without repeating characters.

Example Output:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Solution:

Concept: 
The idea on how to approach this problem is to define the appropriate mapping of each character in your string based on it's index.
This would skip repeated characters in the string to improve the run time of this algorithm. This would result of a time complexity of 
O(n), a space complexity for the Hashmap of O(min(m,n)), and a space complexity for the table of O(m) * m.



Code:

```python
def lengthOfLongestSubstring(self, s: 'str') -> 'int':
    maxlen = 0
    currentlen = 0
    indHash = {}
    leftside = -1
    ls = len(s)
    for ind, ch in enumerate(s):
        if (ch in indHash) and (leftside < indHash[ch]):
            leftside = indHash[ch];
        currentlen = ind - leftside;
        if currentlen > maxlen:
            maxlen = currentlen
        indHash[ch] = ind
    currentlen = ls - leftside - 1
    if currentlen > maxlen:
        maxlen = currentlen
    return maxlen
```
