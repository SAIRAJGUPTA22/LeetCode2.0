class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boat = 0
        left = 0
        n = len(people)
        right = n-1

        while left<=right:
            if people[left]+people[right]<=limit:
                left +=1
            right -=1
            boat +=1
        return boat
