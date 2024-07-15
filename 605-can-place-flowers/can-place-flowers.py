class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if n == 0:
            return True
        for s in range(len(flowerbed)):
           
            if flowerbed[s]==0 and (s==0 or flowerbed[s-1]==0) and (s==len(flowerbed)-1 or flowerbed[s+1]==0):
                flowerbed[s] = 1

                i +=1
                if n== i:
                    return True
                
  