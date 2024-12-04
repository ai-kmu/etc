class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        # 현재 이후 제거
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1  

    def back(self, steps: int) -> str:
        # steps 만큼 이동 , 첫번째 보다 뒤로가지 않게
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # stpes 만큼 이동 마지막 넘지않게
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
