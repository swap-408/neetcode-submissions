class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = 1 + dic.get(i,0)
        sorted(dic)
        
        arr = []
        for num, cnt in dic.items():
            arr.append([cnt,num])
        
        arr.sort()

        res = []
        while len(res) <k:
            res.append(arr.pop()[1])

        return res
        