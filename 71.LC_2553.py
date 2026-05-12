class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []  # res to store
        for num in nums:  # accesing each element of list
            for ch in str(num):  # converting it in string, then accesing its digit
                res.append(int(ch)) # converting in int, then adding to list
        return res

            
