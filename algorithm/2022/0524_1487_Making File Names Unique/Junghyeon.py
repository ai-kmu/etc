class Solution:
    ### feedback ###
    '''
    dictionary 내에 존재할 경우 숫자를 1번부터 탐색 => 중복이 많을 경우 탐색 시간이 오래 걸림
    해결방안: dictionary에 동일 이름이 뜰 경우 해당 value 값을 저장 -> 시작점을 1이 아닌 지금까지의 이름의 개수부터 시작하여 속도 개선 가능
    코드상 수정사항은 2줄 추가
 
    '''
    
    def getFolderNames(self, names):
        name_dict = dict()

        for name in names:
            # 딕셔너리에 없다면 새로 추가
            if name not in name_dict:
                name_dict[name] = 1
            # 이미 딕셔너리에 있는 경우 바뀐 이름을 추가
            else:
                #cnt = 1
                cnt = name_dict[name]                  # 수정사항 [1]
                
                while name + '(' + str(cnt) +')' in name_dict:
                    cnt += 1
                tmp = name + '(' + str(cnt) + ')'
                name_dict[tmp] = 1
                name_dict[name] = name_dict[name] + 1  # 수정사항[2]
                
        # 딕셔너리에 저장된 키 값들을 리턴
        return name_dict.keys()
'''
[결과]
딕셔너리에서 키값들을 비교해가며 업데이트하는 방식
O(n^3)으로 풀이 -> 32번째에서 시간초과...
'''
