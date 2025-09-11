# 238. Product of Array Except Self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixs = []
        sufix = []

        # Calculate all the prefix
        for i in range(len(nums)):
            if i == 0:
                prefixs.append(1)
                continue
            aux = 1
            for j in range(i):
                aux = aux * nums[j]
            prefixs.append(aux)

        # Calculate all the sufix
        for i in range(len(nums)):
            if i == len(nums) - 1:  # last element
                sufix.append(1)
                continue
            aux = 1
            j = len(nums)
            while j > 0:
                aux = aux * nums[j]
                j = j - 1

        return nums
