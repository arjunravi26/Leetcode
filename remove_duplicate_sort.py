#  Remove Duplicates from Sorted Array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        k = 1
        for i in range(1, length):
            # condition to check if the previous element is not equal to current elemet
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k = k+1
        return k

# Create object
sol = Solution()
unique_nos = sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(unique_nos)
