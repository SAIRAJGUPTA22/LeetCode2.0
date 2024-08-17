class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ''
        if str1+str2 == str2+str1:
            
            def gcd(a,b):
                a=len(str1)
                b=len(str2)
                c=min(a,b)
                for i in range(c,0,-1):
                    if (b%i==0) & (a%i ==0):
                        return i
            return str1[:gcd(str1,str2)]


     