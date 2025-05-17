class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # intial_sum = sum(nums[:k])
        # max_sum = intial_sum

        # for i in range(k,len(nums)):
        #     intial_sum += nums[i]-nums[i-k]
        #     max_sum = max(max_sum,intial_sum)
        # return max_sum/float(k)
        # current_sum = sum(nums[:k])
        # max_sum = current_sum
        
        # # Slide the window through the array
        # for i in range(k, len(nums)):
        #     current_sum += nums[i] - nums[i - k]
        #     max_sum = max(max_sum, current_sum)
        
        # Return the maximum average as a float
        # return max_sum / float(k)
        intial_sum = sum(nums[:k])
        max_sum = intial_sum

        for i in range(k,len(nums)):
            intial_sum += nums[i]-nums[i-k]
            max_sum = max(max_sum,intial_sum)
        return max_sum/float(k)