from collections import defaultdict
from copy import deepcopy
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        folder_names=defaultdict(int) # 최종 폴더 딕셔너리 출력. 최종 답에서는 모든 value들이 0이어야 함
        for name in names:
            copy_name = deepcopy(name)
            if copy_name in folder_names: # 이미 folder_name에 있으면
                k = folder_names[copy_name] # 현재 copy_name의 value k를 불러옴
                while copy_name in folder_names: # folder_names에 없을 때까지 k값을 계속 하나씩 늘림
                    k += 1
                    copy_name = f'{name}({k})'
                folder_names[copy_name] = 0 # 수정된 이름 저장
                folder_names[name] = k # 나중에 다시 효율적으로 불러오기 위해 현재 name에 해당되는 k값 저장
            else:
                folder_names[copy_name] = 0 # copy_name이 folder_names에 없으면 바로 저장
        return folder_names.keys()
