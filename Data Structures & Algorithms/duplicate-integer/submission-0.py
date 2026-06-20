class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        available = set()
        for num in nums:
            if num in available:
                return True
            available.add(num)
        return False

