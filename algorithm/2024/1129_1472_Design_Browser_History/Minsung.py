class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_page = homepage  # 현재 page
        self.current_index = -1  # history 내의 현제 page 위치
        self.history = [homepage]  # history 저장

    def visit(self, url: str) -> None:
        if self.current_index == -1:  # visit 시, forward history clear
            self.current_index = len(self.history)-1
        self.history = self.history[:self.current_index+1]
        self.current_page = url
        self.current_index = -1
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.current_index = self.current_index-steps
        if self.current_index * -1 >= len(self.history):  # index 초과 시, 최솟값 지정
            self.current_index = -len(self.history)
        self.current_page = self.history[self.current_index]
        return self.current_page

    def forward(self, steps: int) -> str:
        self.current_index = self.current_index+steps
        if self.current_index >= -1:  # index 초과 시, 최댓값 지정
            self.current_index = -1
        self.current_page = self.history[self.current_index]
        return self.current_page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
