class BrowserHistory(object):
    def __init__(self, homepage):
        # history 방문 기록 리스트
        # c_i 현재 위치 인덱스
        self.history = [homepage]
        self.c_i = 0

    def visit(self, url):
        # 현재 위치 이후의 모든 기록을 제거
        # 방문한 URL을 저장, 현재 위치를 업데이트

        self.history = self.history[:self.c_i + 1]
        self.history.append(url)
        self.c_i += 1

    def back(self, steps):
        # steps만큼 뒤로 이동
        # 최소 0
        self.c_i = max(0, self.c_i - steps)
        return self.history[self.c_i]

    def forward(self, steps):
        # steps만큼 앞으로 이동, 최대 history 수
        self.c_i = min(len(self.history) - 1, self.c_i + steps)
        return self.history[self.c_i]
