class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sumdiv = 1
        for i in range(2, int(num**0.5) + 1):
            if num%i == 0:
                sumdiv += i
                if i != num//i:
                    sumdiv += num//i  # avoid duplicate
        if sumdiv == num:
            return True
        else:
            return False


        #  TC -> O(root n)
        #  SC -> o(1)
