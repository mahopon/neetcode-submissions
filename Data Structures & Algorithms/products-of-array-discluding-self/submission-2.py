class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            l[i] = l[i - 1] * nums[i-1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            r[i] = r[i + 1] * nums[i + 1]
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = l[i] * r[i]

        return res 