class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 단어를 저장할 딕셔너리 설정
        words = dict()

        for i in range(len(strs)):
            # 루프를 돌면서 현재 단어를 가져옴
            curr_word = strs.pop()

            # 가져온 단어를 sorting하여 string으로 키 설정
            key = ''.join(s for s in sorted(curr_word))

            # 만약 해당 key가 words 딕셔너리 안에 없다면 딕셔너리에 키를 새로 생성
            if key not in words:
                words[key] = [curr_word]
            
            # 만약 해당 key가 words 딕셔너리 안에 있다면 딕셔너리의 리스트에 추가
            else:
                words[key].append(curr_word)
        ans = []
        # 생성된 값들을 리스트에 넣어주기
        for v in words.values():
            ans.append(v)
        return ans

