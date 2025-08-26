'''
0. 다음과 같이 약어 정의
    - button 1 = A
    - button 2 = E
    - button 3 = O
    - button 4 = T
    - 추가로, 버튼을 안 누른 상태는 N으로 표기
1. 한 버튼을 두 번 누르면 효과는 사라짐
2. 버튼 누르는 순서는 의미 없음
3. A를 한 번 누르는 것은 OE를 각 한 번 씩 누르는 것과 동일
    - 따라서 버튼은 총 세 개임
=> presses > 3은 그 이하의 경우에서 1을 반복하는 것으로 구현 가능

presses = 0
    - 전부 켜져있는 상태만 가능 (1)
presses = 1
    - 각 버튼을 누른 상태만 가능 (4)
presses = 2
    1. 서로 다른 두 개 누른 상태
        - AO = 101010
        - AE = 010101
        - AT = 100100
        - EO = 000000
        - ET = 001110
        - OT = 110001
    2. 같은 거 두 개 누르기
        - 111111
    - 총 7개
presses = 3
    1. 서로 다른 세 개 누른 상태
        - AEO = 111111
        - AET = 110001
        - AOT = 001110
        - EOT = 100100
    2. 하나를 두 번 누르고, 다른 하나를 누른 상태
        = 하나만 누른 상태
        - A = 000000
        - E = 101010
        - O = 010101
        - T = 011011
    3. 같은 걸 세 번 누른 상태
        = 하나만 누른 상태 (중복)
    - 총 8개
'''


class Solution:
    # 뒤에서부터 세서 몇 번째를 "조작"할 것인지 나타냄
    # 상단 설명과는 방식이 다름
    cands = {
        "N": 0b000000,  # == 같은 거 두 개 / AEO
        "A": 0b111111,  # == EO
        "E": 0b010101,  # == AO
        "O": 0b101010,  # == AE
        "T": 0b001001,
        "AT": 0b110110,  # == EOT
        "ET": 0b011100,  # == AOT
        "OT": 0b100011,  # == AET
    }

    # presses (p) 가 0, 1, 2, 3일 때 가능한 cands 모음
    presses = {
        0: ["N"],
        1: ["A", "E", "O", "T"],
        # 순서대로 AO, AE, AT, EO, ET, OT / N
        2: ["E", "O", "AT", "A", "ET", "OT", "N"],
        # 순서대로 AEO, AET, AOT, EOT / A, E, O, T
        3: ["N", "OT", "ET", "AT", "A", "E", "O", "T"]
    }
    def flipLights(self, n: int, p: int) -> int:
        n = min(n, 6)  # A는 한자리, EO는 두자리, T는 세자리 바꾸니까 6자리만 보면 됨
        p = min(p, 3)  # 위에서 언급했듯 3 초과는 그 이하로 표현 가능

        init = 0b111111  # 초기 상태
        mask = (1 << n) - 1  # n이 6보다 작은 경우 처리하기 위함
        answer = set()
        for press in self.presses[p]:
            answer.add((init ^ self.cands[press]) & mask)
        return len(answer)
