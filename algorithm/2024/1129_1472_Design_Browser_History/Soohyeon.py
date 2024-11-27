class BrowserHistory(object):

    def __init__(self, homepage):
        self.browsers = [homepage]  # 방문 기록 저장
        self.number = 0  # 현재 위치를 나타내는 인덱스

    def visit(self, url):
        # 현재 위치 이후의 기록 삭제
        if self.number + 1 < len(self.browsers):
            self.browsers = self.browsers[:self.number + 1]
        self.browsers.append(url)
        self.number += 1

    def back(self, steps):
        # 뒤로 가기: steps 만큼 이동하거나 0보다 작아지면 기록의 맨 앞까지 이동
        if self.number - steps < 0:
            self.number = 0
        else:
            self.number -= steps
        return self.browsers[self.number]

    def forward(self, steps):
        # 앞으로 가기: steps 만큼 이동하거나 step이 커지면 기록의 맨 끝까지 이동
        if self.number + steps >= len(self.browsers):
            self.number = len(self.browsers) - 1
        else:
            self.number += steps
        return self.browsers[self.number]