class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        from math import gcd
        if str1+str2 == str1+str2:
         def gcd(a, b):
            n1 = max(a, b)
            n2 = min(a, b)
    
            for i in range(n2, 0, -1):
                if n1 % i == 0 and n2 % i == 0:
                    return i  # Return the GCD immediately when condition is met

            return 1  # Fallback case; theoretically, 1 is always a divisor


        return str1[:gcd(len(str1),len(str2))]
        