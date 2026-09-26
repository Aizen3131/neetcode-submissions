class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         dic = {}
         for x in nums:
            if x in dic:

                 dic[x] += 1
            else:
                 dic[x] = 1

         count = 0
         lis = []
         for y, v in sorted(dic.items(), key=lambda y: y[1], reverse=True):
             if count == k:
                 break

             lis.append(y)
             count += 1
         return lis
