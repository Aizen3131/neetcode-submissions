from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            x = target - numbers[i]
            if x in dic:
                # Returns the indices in the correct 1-indexed, increasing order
                return [dic[x] + 1, i + 1]
            dic[numbers[i]] = i
        
        return []