class TimeMap:
    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp: return ""
        arr = self.mp[key]
        l, r = 0, len(arr)-1
        res = None
        while l<=r:
            m = l + (r-l)//2
            if arr[m][0] == timestamp: return arr[m][1]
            elif arr[m][0]<timestamp:
                res = arr[m]
                l = m + 1
            else:
                r = m -1
        if res is None: return ""
        return res[1]
