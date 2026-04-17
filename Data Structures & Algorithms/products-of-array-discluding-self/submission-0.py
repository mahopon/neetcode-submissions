class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            multiply = 1
            for o, num in enumerate(nums):
                if i == o:
                    continue
                multiply = multiply * num
            res.append(multiply)
        return res