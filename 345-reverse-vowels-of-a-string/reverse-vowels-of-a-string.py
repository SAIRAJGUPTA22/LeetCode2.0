class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        i =0 
        e = len(word) - 1
        vowels ="aeiouAEIOU"
        while i < e:
            while i<e and vowels.find(word[i])==-1:
                i += 1
            while i<e and vowels.find(word[e])==-1:
                e -= 1
            word[i],word[e] = word[e],word[i]
            i += 1
            e -= 1
        return "".join(word)
    
    


