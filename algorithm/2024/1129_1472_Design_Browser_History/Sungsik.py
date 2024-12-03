class BrowserHistory:

    def __init__(self, homepage: str):
        self.pointer = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.pointer += 1
        self.history = self.history[:self.pointer]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.pointer -= min(self.pointer, steps)
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer += min(len(self.history)-self.pointer-1, steps)
        return self.history[self.pointer]
