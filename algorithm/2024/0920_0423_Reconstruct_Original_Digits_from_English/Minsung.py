class Solution:
    def originalDigits(self, s: str) -> str:
        '''
        ### Step 1
            - zero ~ nine 중 고유한 알파벳을 가진 digit을 찾음
                - zero(z), two(w) 등
                - 0, 2, 4, 6, 8은 고유한 알파벳을 갖고 있음
                    - s가 위 digit의 고유 알파벳을 포함하는 경우, 해당 digit을 반드시 포함함
                - s의 alpha 목록과 각 수를 기록한 뒤, 위의 digit에 해당하는 alpha 수 차감
        ### Step 2
            - 0, 2, 4, 6, 8을 제외한 나머지 digit들 중에서 고유한 알파벳을 가진 digit을 찾음
                - one(o), three(t) 등
                - 1, 3, 5, 7은 고유한 알파벳을 갖고 있음
                - Step 1과 같은 process
        ### Step 3
            - 9만 유일히 지금까지 고려되지 못했으므로 n'i'ne -> 'i'의 수를 통해 측정함
        '''
        ans = ""
        digit_to_eng = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
        }

        ### Step 1
        digit_to_alpha = dict()
        from collections import defaultdict
        for digit in range(10):  # 각 digit에 해당하는 alpha 목록과 수 기록 
            eng = digit_to_eng[digit]
            digit_to_alpha[digit] = defaultdict(int)
            for alpha in eng:
                digit_to_alpha[digit][alpha] += 1
    
        cur_alpha = defaultdict(int)
        for alpha in s:
            cur_alpha[alpha] += 1  # s가 가지고 있는 alpha 목록과 수 기록

        zero_cnt = cur_alpha['z']
        two_cnt = cur_alpha['w']
        four_cnt = cur_alpha['u']
        six_cnt = cur_alpha['x']
        eight_cnt = cur_alpha['g']

        ans += '0'*zero_cnt + '2'*two_cnt + '4'*four_cnt + '6'*six_cnt + '8'*eight_cnt
        for digit in ans:  # 추가된 digit에 해당하는 alpha 수 차감
            for alpha, cnt in digit_to_alpha[int(digit)].items():
                cur_alpha[alpha] -= cnt  
        
        ### Step 2
        one_cnt = cur_alpha['o']
        three_cnt = cur_alpha['t']
        five_cnt = cur_alpha['f']
        seven_cnt = cur_alpha['s']

        tmp = '1'*one_cnt + '3'*three_cnt + '5'*five_cnt + '7'*seven_cnt
        ans += tmp
        for digit in tmp:
            for alpha, cnt in digit_to_alpha[int(digit)].items():
                cur_alpha[alpha] -= cnt
        
        ### Step 3
        ans += '9'*cur_alpha['i']
        ans = ''.join(sorted(ans))

        return ans
