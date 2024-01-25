# coding challenge 4/366
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# using two pointers method
class solution(object):
  def removeDuplicares(self, nums):
    if not nums:
      return 0
    i = 0
    for j in range(1, len(nums)):
      if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]
      return i +1
    
# using two ponters without checking if the array is empty
class solution(object):
  def removeDuplicares(self, nums):
    j = 0
    for i in range(1, len(nums)):
      if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]
    return i + 1