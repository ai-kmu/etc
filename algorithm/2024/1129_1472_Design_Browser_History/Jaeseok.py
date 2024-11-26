# 쌩 구현으로 풀리는데, 더 효율적인 방법이 있을 것

class BrowserHistory:

    def __init__(self, homepage: str):
        # 히스토리와 현재 방문 위치를 설정
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        # visit을 하면 이후의 히스토리는 지워버림
        self.history = self.history[:self.index + 1]
        self.history.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        self.index -= steps
        # 인덱스가 0보다 작지 않도록 함
        if self.index < 0:
            self.index = 0
        
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index += steps
        # 인덱스가 최대를 넘지 않도록 함
        if self.index >= len(self.history):
            self.index = len(self.history) - 1
        
        return self.history[self.index]
