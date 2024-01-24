# coding challenge 3/366
# https://leetcode.com/problems/two-sum/description/

class Solution(object):
  def twoSum(self, nums, target):
    seen = {}
    for i, num in enumerate(nums):
      complement = target - num
      if complement in seen:
        return [seen[complement], i]
      seen[num] = i
    return []
  
  # alternate solution (brute force)
  
class Solution(object):
  def twoSum(self, nums, target):
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[j] == target - nums[i]:
          return [i, j]