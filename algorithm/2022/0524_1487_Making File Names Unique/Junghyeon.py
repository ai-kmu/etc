class Solution:
    '''
    딕셔너리에서 키값들을 비교해가며 업데이트하는 방식
    O(n^2)으로 풀이 -> 32번째에서 시간초과...
    '''
    def getFolderNames(self, names):
        name_dict = dict()

        for name in names:
            # 딕셔너리에 없다면 새로 추가
            if name not in name_dict:
                name_dict[name] = 1
            # 이미 딕셔너리에 있는 경우 바뀐 이름을 추가
            else:
                cnt = 1
                while name + '(' + str(cnt) +')' in name_dict:
                    cnt += 1
                tmp = name + '(' + str(cnt) + ')'
                name_dict[tmp] = 1
                
        # 딕셔너리에 저장된 키 값들을 리턴
        return name_dict.keys()
