class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(0,len(strs)):
            key = tuple(sorted(strs[i]))
            if key in dic:
                dic[key].append(strs[i])
            else:
                dic[key] = [strs[i]]
        
        return list(dic.values())
        