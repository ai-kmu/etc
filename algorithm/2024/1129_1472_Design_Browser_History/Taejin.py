class BrowserHistory:

    def __init__(self, homepage: str):
        # 초기화. homepage를 가진 urls list 추가, cur_idx 초기화
        self.urls = [homepage]
        self.cur_idx = 0
        
    def visit(self, url: str) -> None:
        # cur_idx 증가, 후의 기록 삭제, url 추가
        self.cur_idx += 1
        self.urls = self.urls[:self.cur_idx]
        self.urls.append(url)
        
    def back(self, steps: int) -> str:
        # steps만큼 cur_idx 위치 변경. (최대 back steps는 0)
        self.cur_idx = max(0, self.cur_idx - steps)
        return self.urls[self.cur_idx]

    def forward(self, steps: int) -> str:
        # steps만큼 cur_dix 위치 변경. (최대 forward steps는 len(self.urls) - 1)
        self.cur_idx = min(len(self.urls) - 1, self.cur_idx + steps)
        return self.urls[self.cur_idx]
