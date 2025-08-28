class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # zero index 기준
        # Button 1 : j = k -> if j (mod 1) = 0 Flip
        # Button 2 : j = 2k + 1 -> if j (mod 2) = 1 Flip
        # Button 3 : j = 2k -> if j (mod 2) = 0 Flip
        # Button 4 : j = 3k -> if j (mod 3) = 0 Flip

        # 1, 2, 3의 lcm으로 변환
        # Button 1 : 6k, 6k + 1, 6k + 2, 6k + 3, 6k + 4, 6k + 5
        # Button 2 : 6k + 1, 6k + 3, 6k + 5
        # Button 3 : 6k, 6k + 2, 6k + 4
        # Button 4 : 6k, 6k + 3

        # 6마다 반복 -> 최대 6자리
        n = min(n, 6)

        # presses : 4번이 최대 선택 경우 (이후는 중복이기 때문)
        # 순서 중요하지 않음
        # presses : 0 -> 1
        # presses : 1 -> 4
        # presses : 2 -> 1(0번) + 6 = 7
        # presses : 3 -> 4(1번) + 4 = 8
        # presses : 4 -> 7(2번) + 1 = 8
        # presses : 5 -> 8(3번)
        # presses : 6 -> 8(4번)
        # presses : 7 -> 8(3번)
        # presses : 8 -> 8(4번)
        presses = min(presses, (presses - 1) % 2 + 3)

        # bit 연산(xor) 활용1 : 최대자리(6)의 버튼 On/Off
        # btn1 : ^ int("111111", 2)
        # btn2 : ^ int("010101", 2)
        # btn3 : ^ int("101010", 2)
        # btn4 : ^ int("100100", 2)
        btn1 = int("111111"[:n], 2)
        btn2 = int("010101"[:n], 2)
        btn3 = int("101010"[:n], 2)
        btn4 = int("100100"[:n], 2)

        # btn_map으로 press별 btn_mask 정의, 최대 2^4 경우.
        btn_map = [
            [0], # press 0
            [btn1, btn2, btn3, btn4], # press 1
            [btn1 ^ btn2, btn1 ^ btn3, btn1 ^ btn4, btn2 ^ btn3, btn2 ^ btn4, btn3 ^ btn4], # press 2
            [btn1 ^ btn2 ^ btn3, btn1 ^ btn2 ^ btn4, btn1 ^ btn3 ^ btn4, btn2 ^ btn3 ^ btn4], # press 3
            [btn1 ^ btn2 ^ btn3 ^ btn4], # press 4 -> bnt4와 동일
        ]

        flips = []

        while presses >= 0:
            for btn_mask in btn_map[presses]:
                flip = int("111111"[:n], 2) ^ btn_mask

                if flip not in flips:
                    flips.append(flip)

            presses -= 2

        return len(flips)
