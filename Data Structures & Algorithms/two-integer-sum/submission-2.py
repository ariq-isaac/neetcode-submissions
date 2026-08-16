class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces = {}
        for index, n in enumerate(nums):
            if target - n in indeces.keys():
                return [indeces[target - n], index]
            else:
                indeces[n] = index
        return []