# 풀이 실패 리뷰 안해주셔도 됩니다

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 각 숫자의 고유 문자를 이용해 몇 번 등장했는지 체크
        count = [0] * 10
        count[0] = s.count('z')  # 0은 'z'를 포함
        count[2] = s.count('w')  # 2는 'w'를 포함
        count[4] = s.count('u')  # 4는 'u'를 포함
        count[6] = s.count('x')  # 6은 'x'를 포함
        count[8] = s.count('g')  # 8은 'g'를 포함

        # 위에서 제거한 문자들을 제외한 나머지 숫자를 찾습니다.
        count[3] = s.count('h') - count[8]  # 3은 'h'를 포함, 하지만 8에서도 'h'가 등장
        count[5] = s.count('f') - count[4]  # 5는 'f'를 포함, 하지만 4에서도 'f'가 등장
        count[7] = s.count('s') - count[6]  # 7은 's'를 포함, 하지만 6에서도 's'가 등장
        count[1] = s.count('o') - count[0] - count[2] - count[4]  # 1은 'o'를 포함, 하지만 0, 2, 4에서도 'o'가 등장
        count[9] = s.count('i') - count[5] - count[6] - count[8]  # 9는 'i'를 포함, 하지만 5, 6, 8에서도 'i'가 등장

        # 숫자를 정렬된 형태로 반환
        result = []
        for i in range(10):
            result.append(str(i) * count[i])
        
        return ''.join(result)
