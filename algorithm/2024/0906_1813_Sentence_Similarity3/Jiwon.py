class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # space 기준으로 분할해서 list로 만들기 (짧은 문장이 sen1)
        if len(sentence1) > len(sentence2):
            sen1 = sentence2.split()
            sen2 = sentence1.split()
        else:
            sen1 = sentence1.split()
            sen2 = sentence2.split()

        # Case 1: 둘 다 길이 1인데 스펠링이 같은 경우만 True
        if len(sen1) == 1 and len(sen2) == 1:
            if sen1[0] == sen2[0]:
                return True

        # Case 2: 짧은 문장 길이만 1이면 짧은 문장에 문장/공백을 넣어 같아질 수 있는지 확인
        elif len(sen1) == 1:
            if sen2[0] == sen1[0] or sen2[-1] == sen1[0]:
                return True

        # Case 3: 둘 다 길이 1이 아닌 경우
        else:
            # 같은 앞 부분 지우기
            short_length = len(sen1)
            for _ in range(short_length):
                if sen1[0] == sen2[0]:
                    del sen1[0]
                    del sen2[0]
                # 안 지워진 sen2를 추가함으로써 동일한 문장 생성 가능
                if len(sen1) == 0:
                    return True

            # 같은 뒷 부분 지우기
            short_length = len(sen1)
            for _ in range(short_length):
                if sen1[-1] == sen2[-1]:
                    del sen1[-1]
                    del sen2[-1]
                # 안 지워진 sen2를 추가함으로써 동일한 문장 생성 가능
                if len(sen1) == 0:
                    return True
                
        return False
