class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
            
        start = 0
        end = len(self.dic[key]) - 1
        mini = -1

        while start <= end:
            middle = (start+end)//2
            if self.dic[key][middle][0] == timestamp:
                return self.dic[key][middle][1]
            elif self.dic[key][middle][0] > timestamp:
                end = middle -1
            else:
                start = middle + 1
                mini = middle
        
        if mini == -1:
            return ""
        else:
            return self.dic[key][mini][1]
