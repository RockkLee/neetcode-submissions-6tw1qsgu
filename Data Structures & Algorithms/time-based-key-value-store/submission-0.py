class TimeMap:

    def __init__(self):
        self.dic: Dict[str, (str, int)] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""

        ls = self.dic[key]
        l = 0
        r = len(ls) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if ls[mid][1] <= timestamp:
                res = ls[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
