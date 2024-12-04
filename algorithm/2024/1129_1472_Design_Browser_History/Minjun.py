# 단순 구현이라서 로직이 동일할 것 같아 주석은 따로 달지 않았읍이다.
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]        
        self.idx = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.idx+1]
        self.history.append(url)
        self.idx = len(self.history)-1
        return None

    def back(self, steps: int) -> str:
        if self.idx - steps > 0:
            self.idx -= steps
            return self.history[self.idx]
        self.idx = 0
        return self.history[self.idx]
    
    def forward(self, steps: int) -> str:
        if self.idx + steps < len(self.history):
            self.idx += steps
            return self.history[self.idx]
        self.idx = len(self.history) - 1
        return self.history[self.idx]
