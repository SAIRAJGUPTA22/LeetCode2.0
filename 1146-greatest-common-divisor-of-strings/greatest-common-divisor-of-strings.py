class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ''
        if str1+str2 == str2+str1:
            n1 = max(len(str1),len(str2))
            n2 = min(len(str1),len(str2))

            def gcd(n1,n2):
                for i in range(n2,0,-1):
                    if n1%i == 0 and n2%i == 0:
                        return i
                return 1
        return  str1[:gcd(n1,n2)]
        