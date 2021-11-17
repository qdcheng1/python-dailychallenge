class Solution:
  
  '''
  Greedy approach, as long as the mx >= last index, return true
  if mx < current index, it means the current index can not be reached
  
  '''
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)):
            if i > mx:
                return False
            if mx >= len(nums) - 1:
                return True
            mx = max(mx, i + nums[i])
        return False
