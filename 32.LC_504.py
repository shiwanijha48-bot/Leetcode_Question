class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:    # if num is 0, then 0
            return "0"
        sign = ""   # store sign(for neg num)
        if num < 0:    # num is neg
            sign = "-"     # save neg sign
            num = -num   # convrt num to +ve
        ans = ""   # empty str to res ans
        while num > 0:    # loop until becomes 0
            ans  = str(num % 7) + ans # get rem (base 7 digit), add  digit to front of res,bcoz digits in rev order 
            num = num//7    # update n by div by 7
        return sign + ans   # add sign if neg + return res
