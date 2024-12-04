class BrowserHistory:

    def __init__(self, homepage: str):
        self.history_stack = []
        self.current_idx = 0

        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.history_stack = self.history_stack[:self.current_idx]

        self.history_stack.append(url)
        self.current_idx += 1

    def back(self, steps: int) -> str:
        target_steps = max(self.current_idx - steps, 1)
        self.current_idx = target_steps

        return self.history_stack[self.current_idx - 1]

    def forward(self, steps: int) -> str:
        target_steps = min(self.current_idx + steps, len(self.history_stack))
        self.current_idx = target_steps

        return self.history_stack[self.current_idx - 1]
