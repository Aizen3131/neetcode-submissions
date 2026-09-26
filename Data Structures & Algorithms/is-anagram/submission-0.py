class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for x in s:
            if x in dic1:
                dic1[x] += 1 
            else:
                dic1[x] = 1
        for y in t:
            if y in dic2:
                dic2[y] += 1 
            else:
                dic2[y] = 1
        
        return dic1 == dic2