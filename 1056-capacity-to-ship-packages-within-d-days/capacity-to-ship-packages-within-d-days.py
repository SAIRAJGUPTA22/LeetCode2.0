class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def s_capacity(capacity):
            need_days = 1
            load = 0
            for weight in weights:
                if load+weight>capacity:
                    need_days += 1
                    load = 0
                load += weight
            return need_days <= days

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left+right)//2
            if s_capacity(mid):
                right = mid -1
            else:
                left = mid+1
        return left
                
        