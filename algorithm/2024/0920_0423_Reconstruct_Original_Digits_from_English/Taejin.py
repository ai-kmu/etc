from collections import deque

class Solution:
    def originalDigits(self, s: str) -> str:
        # ret string, 영어표현 알파벳 리스트 정의, string s에 영어표현 알파벳이 각 몇회씩 포함되는지를 나타내는 사전 정의
        ret = ""
        characters = ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
        characters_dict = dict(zip(characters, [s.count(c) for c in characters]))

        # 탐색을 위한 숫자별 영어표현 리스트와 덱 정의, 빈 리스트 정의
        digits_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        digits = deque(zip(digits_list, [str(i) for i in range(10)]))
        ordered_distinct_digits = []

        # digits이 빌 때까지 반복
        while digits:
            # 반복에서 다른 영어표현들과 구분되는 문자가 있는지 확인
            for _ in range(len(digits)):
                digit, num = digits.popleft()
                complement_digits = "".join([d[0] for d in digits])
                distinct_characters = list(set(digit) - set(complement_digits))
                
                # 1 이상이면 존재하는 digits에서 다른 english represantation의 element set과 구분이 되는 것이므로
                # ordered_distnct_digits에 추가
                if len(distinct_characters) >= 1: 
                    ordered_distinct_digits.append([digit, min(distinct_characters, key=lambda x:digit.count(x)), str(num)])
                    continue
                
                # 1 미만이면 구분되는 문자가 없으므로 다시 추가
                digits.append([digit, num])
        
        # ordered_distinct_digits를 탐색하며 영어표현 문자 키에 구분되는 문자 개수만큼 빼줌
        for d, distinct_c, num in ordered_distinct_digits:
            cnt = characters_dict[distinct_c]
            ret += num * cnt

            for c in d:
                characters_dict[c] -= cnt

        return "".join(sorted(ret))
