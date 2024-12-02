class BrowserHistory:
    """
    self.history : 홈페이지를 방문한 순으로 기록 (`{index: url}`)
    self.curr_pg : 현재 있는 홈페이지 인덱스
    self.max_num : history에 있는 최대 페이지 개수
    """

    def __init__(self, homepage: str):
        """`0`번 인덱스에 인자로 입력된 `homepage` 저장"""
        self.history = {0: homepage}
        self.curr_pg = 0
        self.max_num = 0

    def visit(self, url: str) -> None:
        """
        인덱스와 페이지 개수 하나 늘리고, `self.history` 업데이트
        만약 `visit` 메서드 호출 전에 `self.curr_pg`가 `self.max_num`보다 작다면
            -> `self.history` 덮어쓰기 + 이후 기록 접근 불가 (`self.max_num` 초기화)
        """
        self.curr_pg += 1
        self.max_num = self.curr_pg
        self.history[self.curr_pg] = url

    def back(self, steps: int) -> str:
        # step만큼 이동하지만 0보다는 작아질 순 없음
        self.curr_pg = max(self.curr_pg - steps, 0)
        return self.history[self.curr_pg]

    def forward(self, steps: int) -> str:
        # step만큼 이동하지만 `self.max_num`보다는 작아질 순 없음
        self.curr_pg = min(self.curr_pg + steps, self.max_num)
        return self.history[self.curr_pg]
