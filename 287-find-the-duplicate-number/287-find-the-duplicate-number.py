class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=nums[slow]
        while(slow!=fast):
            slow=nums[slow]
            fast=nums[nums[fast]]
        slow=0
        while(slow!=nums[fast]):
            slow=nums[slow]
            fast=nums[fast]
        return slow
        