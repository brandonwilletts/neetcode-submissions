class TimeMap:

    def __init__(self):
        # "alice": [[1, "happy"], [2, "sad"], ...]
        self.hashmap = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        output = ""
        values = self.hashmap.get(key, [])

        l, r = 0, len(values) - 1
    
        while l <= r:
            mid = (l + r) // 2

            if timestamp == values[mid][0]:
                return values[mid][1] 

            if timestamp > values[mid][0]:
                output = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return output