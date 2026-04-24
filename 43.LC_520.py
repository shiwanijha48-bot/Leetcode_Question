class Solution:
        def all_upper(self, word):
            for ch in word:
                if not ('A' <= ch <= 'Z'):
                    return False
            return True
        def all_lower(self, word):
            for ch in word:
                if not ('a' <= ch <= 'z'):
                    return False
            return True
        def captalize_letter(self, word):
            if not ('A' <= word[0] <= 'Z'):
                return False
            for ch in word[1:]:
                if not('a' <= ch <= 'z'):
                    return False
            return True
        def detectCapitalUse(self, word: str) -> bool:
            return self.all_upper(word) or self.all_lower(word) or self.captalize_letter(word)

# return word.isupper() or word.islower() or word.istitle()
        
