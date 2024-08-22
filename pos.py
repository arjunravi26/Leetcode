# 35. Search Insert Position
# Solved
# Easy
# Topics
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index,num in enumerate(nums):
            if num == target or num > target:
                return index
        return index+1
    
obj = Solution()
index = obj.searchInsert([1,2,3,6,7,8],5)
print(index)