class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        
        for i in range(len(nums)):
            if target - nums[i] in index_map:
                return [index_map[target - nums[i]], i]
            index_map[nums[i]] = i
        return []
