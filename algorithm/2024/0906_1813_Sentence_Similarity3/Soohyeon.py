# 풀이 실패..
class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        
        result = True
        sentence1_parsing = sentence1.split()
        sentence2_parsing = sentence2.split()

        if len(sentence1_parsing) < len(sentence2_parsing):
            sentence1_parsing = sentence2.split()
            sentence2_parsing = sentence1.split()

        if len(sentence1_parsing) == len(sentence2_parsing):
            return sentence1 == sentence2

        i = j = 0
        in_list = []
        reverse = -1
        qweqwe = 0

        for _ in range(len(sentence2_parsing)):
            if sentence2_parsing[reverse] == sentence1_parsing[reverse]:
                reverse -= 1
                qweqwe += 1

        if qweqwe == len(sentence2_parsing):
            return True
        
        if (len(sentence2_parsing) == 1) and (sentence2_parsing[0] == sentence1_parsing[0] or sentence2_parsing[0] == sentence1_parsing[-1]):
            return True

        else:
            for _ in range(len(sentence1_parsing)):
                if sentence1_parsing[i] == sentence2_parsing[j]:
                    i += 1
                    j += 1
                    in_list.append(i-1)
                    if j == len(sentence2_parsing):
                        break 
                elif sentence1_parsing[i] != sentence2_parsing[j]:
                    i += 1
                    if i == len(sentence1_parsing):
                        return False

        if len(in_list) == 1:
            if (0 in in_list) or (len(sentence1_parsing) - 1 in in_list) and (len(in_list) == len(sentence2_parsing)):
                result = True
            else:
                result = False

        else:
            stack = 0
            if in_list[0] != 0:
                stack += 1
            if in_list[-1] != len(sentence1_parsing) -1:
                stack += 1
            for number in range(len(in_list) - 1):
                if in_list[number + 1] - in_list[number] > 1:
                    stack += 1
            if stack >= 2:
                result = False

        return result


# 솔루션 참조
# 서로의 길이를 비교해서 길이가 짧은것을 2로 둠
# 앞에서부터 비교해서 같으면 i를 늘려줌
# 뒤에서 부터 공통된 단어의 갯수를 세주며 j를 늘려줌
# i + j가 n보다 크거나 같으면 두 문장은 유사하다고 판단

class Solution:
    def areSentencesSimilar(self, sentence1, sentence2):
        words1, words2 = sentence1.split(), sentence2.split()
        m, n = len(words1), len(words2)
        if m < n:
            words1, words2 = words2, words1
            m, n = n, m
        i = j = 0
        while i < n and words1[i] == words2[i]:
            i += 1
        while j < n and words1[m - 1 - j] == words2[n - 1 - j]:
            j += 1
        return i + j >= n
    