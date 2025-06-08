class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        chars = [i.lower() for i in licensePlate if i.isalpha()]
        required = Counter(chars)
        min_length =float('inf')
        shortword = None

        for word in words:
            word_counts = Counter(word)
            Valid = True

            for char, count in required.items():
                if word_counts.get(char,0)<count:
                    Valid = False
                    break
            if Valid:
                if len(word)< min_length:
                    shortword = word
                    min_length = len(word)
        
        return shortword