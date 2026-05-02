class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0 # stores valid rotated numbers
        for i in range(1, n+1): # check every number from 1 to n
            s = str(i) # convert number to string for digit checking
            # skip number if it contains any invalid digit (3, 4, 7)
            if any(ch in '347' for ch in s):
                continue
            # count number if it has at least one digit that changes on rotation (2,5,6,9)
            if any(ch in '2569' for ch in s):
                count += 1
        return count
# ------------------------------------------------------------------------------------------
class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0 # stores valid rotated numbers
        for i in range(1, n+1): # check every number from 1 to n
            s = str(i) # convert number to string for digit checking
             # check invalid digits (3,4,7) → number becomes invalid
            flag_invalid = False
            for ch in s:
                if ch in '347':
                    flag_invalid = True
                    break
            if flag_invalid:
                continue  # skip this number
            # check if number changes after rotation (must have 2,5,6,9)
            flag_valid = False
            for ch in s:
                if ch in '2569':
                    flag_valid = True
                    break
            if flag_valid:
                count += 1  # valid rotated number
        return count
            
