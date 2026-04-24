class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10 :  #repeat till num becomes single digit
            sumDigits = 0  #reset sum for each iteration
            while num > 0:  # extract and add digits of current number
                ld = num % 10   # last digit
                sumDigits += ld  # add last digit
                num = num//10   # remove ld
            num = sumDigits  # updaytw num with sod
        return num
#  TC -> O(d) d = no of digits
#  SC-> 0(1)
