class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)  # total len
        res = []   # res arr
        posnum = []    # list of positive num
        negnum = []    # list of negative num
        for i in range(0, n):
            if nums[i] > 0:  # finding pos num, and storing
                posnum.append(nums[i])
            if nums[i] < 0:  # finding neg num, and storing
                negnum.append(nums[i])
        k = len(posnum)   # or len(negnum) # len of posnum and negnum are same.. equal h dono so kisi ek ka len le sakte h
        for i in range(k):   # merging the both array alternatively
            res.append(posnum[i])
            res.append(negnum[i])
        return res

  # ---------------------------------------------------------------------------------------------------

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        posindex, negindex = 0, 1
        for i in range(0,n):
            if nums[i] >= 0:
                res[posindex] = nums[i]
                posindex += 2
            else:
                res[negindex] = nums[i]
                negindex += 2
        return res

  # ----------------------------------------------------------------------------------------------------

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        n = len(nums)
        for i in range(0, len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        for i in range(len(pos)):
            nums[2 * i] = pos[i]
            nums[(2*i) + 1] = neg[i]
        return nums
