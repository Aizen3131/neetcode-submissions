class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        answers = set()

        for i in range(len(nums)):
            first = nums[i]
            seen = set()

            for x in range(i + 1, len(nums)):
                second = nums[x]

                have = first + second
                missing = target - have   # what we still need to reach 0

                if missing in seen:
                    triplet = sorted([first, second, missing])
                    answers.add(tuple(triplet))

                seen.add(second)

        return [list(t) for t in answers]