class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # 파일 이름을 세는 딕셔너리 생성
        count_names = {}
        ans = [""]*len(names)
        for idx, name in enumerate(names):
            # name이 딕셔너리에 있으면 이름에 + (번호)를 해서 정답 리스트에 저장
            if name in count_names:
                name_num = count_names[name]
                only_name = name
                # 딕셔너리에 이름이 있을 경우 저장할 번호를 현재 인덱스 값으로 넣는다
                # (시작 인덱스가 1이기 때문에 현재 인덱스는 저장된 인덱스 + 1된 값)
                while name in count_names:
                    name = only_name + f"({name_num})"
                    name_num += 1
                count_names[only_name] = name_num
                count_names[name] = 1
            # 만약 name이 없으면 새로 이름 만들어서 1로 초기화
            # 이후 정답 리스트에 이름만 저장
            else:
                count_names[name] = 1
            ans[idx] = name
        return ans
