class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []  # lst to store the 1s count of each num from 0 to n
        for i in range(0, n+1): # 0 to n
            b = bin(i)   # convert each into binary # 0b-01101..
            count = 0
            for ch in b:   # each char of binary conversion of each num
                if ch == '1':  
                    count += 1
            ans.append(count)  # append 1s count of each bin curr num
        return ans
  
