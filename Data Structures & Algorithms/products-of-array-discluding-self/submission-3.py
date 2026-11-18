class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1] * len(nums)

        i = 1
        j = len(nums)-2

        while i < len(nums) and j >= 0:
            left[i] = left[i-1]*nums[i-1]
            right[j] = right[j+1]*nums[j+1]
            i += 1
            j -= 1
        res = []

        

        for i in range(len(nums)):
            left_product = left[i]
            right_product = right[i]
            self_product = left_product * right_product

            res.append(self_product)

        return res  
                