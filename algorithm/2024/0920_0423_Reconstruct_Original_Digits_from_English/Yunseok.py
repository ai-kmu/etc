## 문제 이해에 어려움을 겪어서, 문제 설명과 관련된 자료 참고하였음

from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        letter_count = Counter(s)
        
        # 각 숫자에 대응하는 개수를 저장할 리스트, 0부터 9까지의 숫자를 나타냄.
        digit_count = [0] * 10
        
        # 유일한 문자로 나타나는 숫자들을 먼저 찾는다.
        digit_count[0] = letter_count.get('z', 0)
        digit_count[2] = letter_count.get('w', 0)
        digit_count[4] = letter_count.get('u', 0)
        digit_count[6] = letter_count.get('x', 0)
        digit_count[8] = letter_count.get('g', 0)
        
        # 이미 찾은 숫자들을 제외한 나머지 숫자들을 처리
        digit_count[3] = letter_count.get('h', 0) - digit_count[8]  # 'h'는 8과 3에서 등장
        digit_count[5] = letter_count.get('f', 0) - digit_count[4]  # 'f'는 4와 5에서 등장
        digit_count[7] = letter_count.get('s', 0) - digit_count[6]  # 's'는 6과 7에서 등장
        digit_count[9] = letter_count.get('i', 0) - digit_count[5] - digit_count[6] - digit_count[8]  # 'i'는 여러 숫자에서 등장
        digit_count[1] = letter_count.get('o', 0) - digit_count[0] - digit_count[2] - digit_count[4]  # 'o'는 0, 1, 2, 4에서 등장
        
        # 결과 문자열을 구성하여 반환
        result = []
        for i, count in enumerate(digit_count):
            if count > 0:
                result.append(str(i) * count)
        
        return ''.join(result)
