class AllOne:

    def __init__(self):
        self.h = {}
        

    def inc(self, key: str) -> None:
        if key in self.h:
            self.h[key] += 1
        else:
            self.h[key] = 1

    def dec(self, key: str) -> None:
        if key in self.h:
            if self.h[key] > 1:
                self.h[key] -= 1
            else:
                del self.h[key]

    def getMaxKey(self) -> str:
        if not self.h:
            return ""
        return max(self.h, key=self.h.get)

    def getMinKey(self) -> str:
        if not self.h:
            return ""
        return min(self.h, key=self.h.get)