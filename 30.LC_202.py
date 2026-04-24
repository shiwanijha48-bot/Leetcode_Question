class Solution:
    def isHappy(self, n: int) -> bool:
        exists = set()  # to track visited numbers,detect cycle
        while n != 1 and n not in exists: # loop until n becomes 1(happy no) or n repeats(cycle= not happy)
            exists.add(n) # store curr val of n
            x = 0  # storr sum of sq of digits
            temp = n # orgnl val
            while n > 0:  # extract each digit
                ld = n % 10   # lastr digit
                x = x + ld*ld   # sum of sq of digits
                n = n//10   # remove last digivt
            n = x  # update n with new val
        if n == 1:  #  happy number
            return True
        else:   # cycyle detected
            return False
    
