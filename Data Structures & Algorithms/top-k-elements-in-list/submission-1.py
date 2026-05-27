class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for num in nums:
            numDict[num] = 1 if num not in numDict else numDict[num] + 1

        #print(numDict)
        res = []
        for i in range(k):
            maxNumVal = -1001
            maxNum = -100
            for num in numDict:
                #print(f"Adding in num: {num} with freq: {numDict[num]}")
                if numDict[num] > maxNumVal and (num not in res):
                    maxNumVal = numDict[num]
                    maxNum = num
                    #print(f"max num is {maxNum}")
            res.append(maxNum)
    
        return res
        
        