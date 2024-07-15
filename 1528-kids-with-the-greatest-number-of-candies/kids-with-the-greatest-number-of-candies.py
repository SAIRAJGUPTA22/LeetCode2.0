class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = max(candies)
        b=[]
        for i in candies:
            if i + extraCandies >= a:
               
                b.append(True)
            else:
                b.append(False)
        return b
