class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_inds = []
        vowels = []
        for i, c in enumerate(s):
            # 대문자, 소문자 모음인 경우 인덱스 정보와 알파벳 저장
            if c in 'aeiouAEIOU':
                vowels.append(c)
                vowels_inds.append(i)
        # sorted 함수로 key lambda를 이용하여 ascii code 오름차순으로 정렬
        # ord 함수를 이용하여 정렬 가능
        vowels = sorted(vowels, key = lambda x : ord(x))

        # 입력 s를 리스트 형태로 변환
        list_s = list(s)

        # 정렬된 vowel과 저장된 인덱스 정보인 vowels_inds를 이용해 조건에 맞게 모음 정렬
        for i, ind in enumerate(vowels_inds):
            list_s[ind] = vowels[i]

        return "".join(list_s)
