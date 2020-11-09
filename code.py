class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        h = {}
        if(len(nums) == 0):
            return []
        for i in range(len(nums)):
            if(nums[i] not in h):
                h[nums[i]] = 1
            else:
                result.append(nums[i])
            
        return result
