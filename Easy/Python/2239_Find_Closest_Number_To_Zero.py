def findClosestNumber(self, nums: List[int]) -> int:
        ret = float('inf')
        for num in nums:
            if abs(num) < abs(ret):
                ret = num
            elif abs(num) == abs(ret):
                ret = max(ret,num)
        return ret

#Solution video: https://youtu.be/S5rKDCUOWO4 
