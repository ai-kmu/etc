# solution 참조
# https://saurus2.tistory.com/entry/LeedCode-423-Reconstruct-Original-Digits-from-English-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Medium

class Solution:
    def originalDigits(self, s: str) -> str:
        # 각 숫자를 고유하게 식별할 수 있는 문자들
        uniq = ['z', 'w', 'u', 'x', 'g']
        
        # 각 숫자의 개수를 저장할 리스트
        num = []
        
        # 고유 문자의 개수를 세기
        z = s.count('z')  # 'z' -> 0
        w = s.count('w')  # 'w' -> 2
        u = s.count('u')  # 'u' -> 4
        f = s.count('f') - u  # 'f' -> 5, 'u'의 개수만큼 뺌
        x = s.count('x')  # 'x' -> 6
        v = s.count('v') - f  # 'v' -> 7, 'f'의 개수만큼 뺌
        g = s.count('g')  # 'g' -> 8
        r = s.count('r') - z - u  # 'r' -> 3, 'z'와 'u'의 개수만큼 뺌
        o = s.count('o') - z - w - u  # 'o' -> 1, 'z', 'w', 'u'의 개수만큼 뺌
        n = (s.count('n') - v - o) // 2  # 'n' -> 9, 쌍으로 고려

        # 최종 숫자 문자열 생성
        return (
            '0' * z +
            '1' * o +
            '2' * w +
            '3' * r +
            '4' * u +
            '5' * f +
            '6' * x +
            '7' * v +
            '8' * g +
            '9' * n
        )
