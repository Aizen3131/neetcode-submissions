from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Format per string: <length>#<string>
        """
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1
            
            # Read the string length preceeding '#'
            length = int(s[i:j])
            
            # Extract the string of length `length` starting after '#'
            start = j + 1
            res.append(s[start : start + length])
            
            # Move index past the extracted string
            i = start + length
            
        return res
