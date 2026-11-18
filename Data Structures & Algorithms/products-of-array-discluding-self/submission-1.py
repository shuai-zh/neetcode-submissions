class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1] * len(nums)

        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]

        res = []

        for i in range(len(nums)):
            left_product = left[i]
            right_product = right[i]
            self_product = left_product * right_product

            res.append(self_product)

        return res  
                