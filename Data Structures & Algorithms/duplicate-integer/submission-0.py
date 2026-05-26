class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numsDict = {}
        for i, num in enumerate(nums):
            if num in numsDict:
                return True
            else:
                numsDict[num] = i
        return False

            