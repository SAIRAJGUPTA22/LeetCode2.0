class Solution:
    def reverseVowels(self, s: str) -> str:
        Vowels = 'aeiouAEIOU'
        left = 0
        right = len(s)-1
        s = list(s)
        while left < right:
            if s[left] in Vowels and s[right] in Vowels:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            elif s[left] not in Vowels:
                    left += 1
            elif s[right] not in Vowels:
                    right -= 1
        return ''.join(s)
                

        