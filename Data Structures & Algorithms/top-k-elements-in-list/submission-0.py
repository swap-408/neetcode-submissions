class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1
        sorted(dic)
        res = sorted(dic, key = lambda key: dic[key], reverse= True)

        return res[0:k];
        
        