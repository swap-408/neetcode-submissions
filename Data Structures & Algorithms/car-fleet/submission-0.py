class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = []
        for i in range(len(position)):
            l.append([position[i],speed[i]])
        l.sort(reverse=True)
        prev = l[0]
        count =1
        for c in range(1,len(l)):
            tp = (target-prev[0])/prev[1]
            tc = (target-l[c][0])/l[c][1]

            if tp<tc:
                count += 1
                prev = l[c]
        return count