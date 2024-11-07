class Solution:
    def reverseVowels(self, s: str) -> str:
        Vowels = 'aeiouAEIOU'
        vow = []
        v = [ c for c in s if c in Vowels]
        for c in s:
            if c in Vowels:
                vow.append(v.pop())
            else:
                vow.append(c)
        return ''.join(vow)
        
