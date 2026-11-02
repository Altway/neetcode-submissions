class Solution:
    def bak_productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        while(i!=len(nums)):
            total_fold = 1
            for el in nums[:i]+nums[i+1:]:
                total_fold *= el
            output.append(total_fold)
            i+=1
        return output
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fold_list = [1]
        fold_total = 1
        for num in nums:
            fold_total *= num
            fold_list.append(fold_total)
        inv_fold_list = [1]
        fold_total = 1
        for num in nums[::-1]:
            fold_total *= num
            inv_fold_list.append(fold_total)        

        output = []
        for i in range(len(nums)):
            output.append(fold_list[i]*inv_fold_list[len(nums)-i-1])
        return output