class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = False
        check = set()
        for i in range (len(nums)): 
            if nums[i] in check: 
                answer = True;
            check.add(nums[i])
            

        return answer

