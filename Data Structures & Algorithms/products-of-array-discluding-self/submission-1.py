class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums)):
            for o in range(len(nums)):
                if i == o:
                    continue
                res[i] = res[i] * nums[o]
        return res
            