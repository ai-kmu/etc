# slicing window

from collections import Counter

class Solution:
    def min_window(self, big_string: str, small_string: str) -> str:
        small_dict = Counter(small_string)
        big_dict = {}
        need_to_find = len(small_string)

        left = 0 
        right = 0
        answer = ""

        while right < len(big_string):  
            right_char = big_string[right]  # 현재 오른쪽 포인터의 문자
            if right_char in big_dict:
                big_dict[right_char] += 1  # 이미 있는 문자는 +1 증가
            else:
                big_dict[right_char] = 1  # 처음 등장하는 문자는 1로 초기화

            if right_char in small_dict:  # 찾고자 하는 문자일 경우
                if big_dict[right_char] <= small_dict[right_char]:  
                    need_to_find -= 1  # 필요한 문자 개수 줄이기

            while need_to_find == 0:  # 필요한 문자를 다 찾았을 경우
                left_char = big_string[left]  # 현재 왼쪽 포인터의 문자

                big_dict[left_char] -= 1  # 윈도우에서 문자 제거
                if left_char in small_dict:  
                    if big_dict[left_char] < small_dict[left_char]:  
                        # 최소 윈도우를 갱신
                        if answer == "":  
                            answer = big_string[left:right+1]  # 첫 번째 결과 저장
                        elif len(answer) > (right - left):  
                            answer = big_string[left:right+1]  # 더 작은 윈도우 발견 시 갱신
                        need_to_find += 1  # 다시 찾아야 할 문자 개수 증가

                left += 1  # 왼쪽 포인터 이동
            right += 1  # 오른쪽 포인터 이동

        return answer  # 최종 결과 반환
