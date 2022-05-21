#### 정답 코드
#### 문제가 생각했던 내용이랑 조금 다르게 평가를 진행(접미사를 붙인 것들을 구분하지 않음)
class Solution:
    def getFolderNames(self, names):

        name_list = {} # Hash Table 생성
        result = []    # output list 생성

        for name in names:

            # 해당 이름이 Table에 존재하지 않으면 추가 
            if name not in name_list:
                name_list[name] = 1
                result.append(name)

            # 해당 이름이 Table에 존재할 경우 몇개 존재하는지 확인
            else: 
                cnt = name_list[name]  # 중간 오류 해결(여러번 동일한 이름이 등장할 경우 dictionary 수로 갱신)

                # 반복문 진행하면서 숫자 접미사를 확인(등장했다면 => 숫자를 추가해서 다시 탐색 / 등장하지 않는다면 종료) 
                while True:            
                    if name + '(' + str(cnt) +')' in name_list:
                        cnt = cnt + 1
                    else:
                        break
                new_name =  name + '(' + str(cnt) +')'

                result.append(new_name)
                name_list[name] = name_list[name] + 1      # 이름 (혹은 이름 + 접미사) 부분을 cnt를 갱신해줘야함 
                name_list[new_name] = 1                    # 새롭게 만든 이름 + 접미사를 dictionary에 추가해줘야함 (error 발생)
                
        return result
