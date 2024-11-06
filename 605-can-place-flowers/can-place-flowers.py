class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if n == 0:
            return True
        for s in range(len(flowerbed)):
            if (flowerbed[s] == 0) and (flowerbed[s-1]==0 or s==0) and (s==len(flowerbed)-1 or flowerbed[s+1]==0):
                flowerbed[s]=1
                i += 1
                if i == n:
                    return True
        return False
                
  
        