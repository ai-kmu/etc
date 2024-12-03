class BrowserHistory:

    def __init__(self, homepage: str):
        self.url = homepage
        self.pointer = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.url = url
        self.pointer += 1
        self.history = self.history[:self.pointer]
        self.history.append(self.url)

    def back(self, steps: int) -> str:
        self.pointer -= min(self.pointer, steps)
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer += min(len(self.history)-self.pointer-1, steps)
        return self.history[self.pointer]
