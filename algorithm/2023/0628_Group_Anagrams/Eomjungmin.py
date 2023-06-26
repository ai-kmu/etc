class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {} # 그룹별로 저장할 딕셔너리 선언
        for w in strs:
            group_strs = "".join(sorted(w)) # group_strs: 같은 철자로만 구성된 그룹 (정렬함으로써 str에 있는 단어들을 그룹 단위로 분류)
            # w(strs안 한 단어)를 group_strs에 맞춰서 딕셔너리의 value로 저장
            # group_strs가 dict_에 없으면 새로 리스트 안에 w 넣어서 선언
            # group_strs가 dict_에 있으면 리스트에 append하여 w 추가
            if group_strs in dict_:
                dict_[group_strs].append(w)
            else:
                dict_[group_strs] = [w]

        return dict_.values()
