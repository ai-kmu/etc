class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack=[homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.curr+1]
        self.curr += 1
        self.stack.append(url)

    def back(self, steps: int) -> str:
       
        if steps <= self.curr:
            self.curr -= steps
        else:
            self.curr = 0
   
        return self.stack[self.curr]

    def forward(self, steps: int) -> str:
        if self.curr + steps < len(self.stack):
            self.curr += steps
        else:
            self.curr = len(self.stack) - 1
        return self.stack[self.curr]
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
