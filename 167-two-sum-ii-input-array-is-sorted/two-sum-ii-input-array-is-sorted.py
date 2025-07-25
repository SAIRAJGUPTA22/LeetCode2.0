class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0 
        right = len(numbers)-1

        while left<=right:
            current_sum =  numbers[left]+numbers[right]
            if current_sum == target:
                return [left+1,right+1]
            elif current_sum < target:
                left = left+1
            else:
                right = right -1
        return [-1,-1]