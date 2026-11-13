class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()

        for num in nums:
            if num not in uniqueSet:
                uniqueSet.add(num)
            else:
                return True
        return False