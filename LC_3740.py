class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ele = {}   # dict store val,indices 
        for i in range(0, len(nums)):   # store indices of each val
            if nums[i] in ele:   # val exists in dict
                ele[nums[i]].append(i)   # append curr ind to lst
                #--- { 1:[0,2,3], 2:[1], 3:[4] } ----
            else:   # val sbsent, new lst with ind
                ele[nums[i]] = [i]

        ans = float('inf')   # inf as want min
        for key in ele:   # loop through each unique val
            sameVal = ele[key]   # lst of indices val occurs = [0,2,3]
            if len(sameVal) >= 3:    # atleast 3 occurences eixts
                for i in range(len(sameVal)-2):   # consecutive triplet
                #--- len = 3, range(1)= only i = 0
                    a = sameVal[i]   # 1st ind
                    b = sameVal[i+1]   # 2nd ind
                    c = sameVal[i+2]   # 3rd ind
                    dist = abs(a-b) + abs(b-c) + abs(c-a)
                    ans = min(ans, dist)   # update min dist min(inf, 6)
            
        if ans == float('inf'):   # no valid triplet
            return -1
        else:
            return ans
