from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for x in strs:
            key = tuple(sorted(x))  # Using tuple as the key
            if key in dic:
                dic[key].append(x)
            else:
                dic[key] = [x]

        # Explicitly iterating through the dictionary at the end
        lis = []
        for v in dic.values():
            lis.append(v)
            
        return lis


        