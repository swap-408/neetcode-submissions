class MedianFinder:

    def __init__(self):
        self.count = 0
        self.leftHalf = []
        self.rightHalf = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHalf, -num)
        self.count += 1
        
        if self.rightHalf and -self.leftHalf[0]>self.rightHalf[0]:
            heapq.heappush(self.rightHalf,-heapq.heappop(self.leftHalf))
        
        if len(self.leftHalf)-len(self.rightHalf)>1:
            heapq.heappush(self.rightHalf,-heapq.heappop(self.leftHalf))
        if len(self.rightHalf)>len(self.leftHalf):
            heapq.heappush(self.leftHalf,-heapq.heappop(self.rightHalf))

    def findMedian(self) -> float:
        
        
        l = self.leftHalf[0]
        if self.count%2 == 1: return -l
        r = self.rightHalf[0]
        return (r-l)/2
        