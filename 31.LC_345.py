class Solution:
    def reverseVowels(self, s: str) -> str:
        r = ""  # res str final ans
        v = {'a','e','i','o','u','A', 'E','O','U','I'} # set of vowels(lc & uc)
        vowels = []  # list store vowels in str
        for i in s: # iterate char in str
            if i in v:
                vowels.append(i) # if chr in vowel, store in vowel lst
        vowels = vowels[::-1] # rev collected vowels
        j = 0   # ptr
        for i in s:  # iterate org str
            if i not in v:
                r = r + i # if not vowel, add char as it is
            else:
                r = r + vowels[j] # if vowel, take nxt vwl from rev lst
                j += 1  # move to nxt vwl in rev lst
        return r  # return final str with vwl rev
