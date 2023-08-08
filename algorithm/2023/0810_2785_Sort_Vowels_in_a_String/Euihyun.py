class Solution(object):
    def sortVowels(self, s):
        # 입력 문자열에서 모음을 찾아내기 위해 모음 집합 생성
        vowels = set('aeiouAEIOU')
        
        # 모음과 비모음을 따로 저장할 리스트 생성
        vowels_list = []
        consonants_list = []
        
        # 입력 문자열을 순회하며 모음과 비모음 분리
        for char in s:
            if char in vowels:  # 모음이면 모음 리스트에 추가
                vowels_list.append(char)
            else:  # 비모음이면 비모음 리스트에 추가
                consonants_list.append(char)
        
        # 모음 리스트 정렬
        vowels_list.sort()
        
        # 결과를 저장할 리스트 초기화
        t = []
        vowel_index = 0  # 모음 리스트에서의 인덱스
        consonant_index = 0  # 비모음 리스트에서의 인덱스
        
        # 입력 문자열을 순회하며 모음과 비모음을 정렬된 리스트의 원소로 대체하여 결과 리스트에 추가
        for char in s:
            if char in vowels:  # 모음이면 정렬된 모음으로 대체하여 결과 리스트에 추가
                t.append(vowels_list[vowel_index])
                vowel_index += 1
            else:  # 비모음이면 정렬된 비모음으로 대체하여 결과 리스트에 추가
                t.append(consonants_list[consonant_index])
                consonant_index += 1
        
        # 결과 리스트의 문자들을 이어붙여 하나의 문자열로 만들어 반환
        return ''.join(t)
