class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        st1_list = sentence1.split(' ')
        st2_list = sentence2.split(' ')

        # 두 리스트 중 짧은 것과 긴 것을 구분
        if len(st1_list) > len(st2_list):
            pivot_list = st1_list
            other_list = st2_list
        else:
            pivot_list = st2_list
            other_list = st1_list

        i = 0
        while i < len(other_list) and other_list[i] == pivot_list[i]:
            i += 1

        j = 0
        while j < len(other_list) - i and other_list[-(j + 1)] == pivot_list[-(j + 1)]:
            j += 1

        # 앞, 뒤에서 일치한 단어 수 == 전체 단어 수이면 True 반환
        return i + j == len(other_list)
