class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        
        duplicates = {}

        for num in nums:
            if num in duplicates:
                return True
            
            duplicates[num] = num

        return False