class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # 해시함수 활용
        file = {}
        
        for name in names:
            # 맵핑
            if name not in file:
                file[name] = 1
                continue
            
            # 중복된다면,
            else:
                # 중복 회피용 폴더 이름에 쓰일 k 값 초기화
                # 첫 중복이라면 value = 1, 
                # 두번째 등장부터는 value값으로 체크한 중복 횟수로 초기화 --> 시간 단축
                k = file[name]
                new_name = name + '(' + str(k) + ')'
                
                while new_name in file:
                    k += 1
                    new_name = name + '(' + str(k) + ')'
                
                # 중복 벗어났다면 새로 맵핑
                file[new_name] = 1
                
                # 확인한 중복 횟수 업데이트
                file[name] += 1
                
        return file.keys()
                        
                           
