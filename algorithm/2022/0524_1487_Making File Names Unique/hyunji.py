# 오답코드

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        files = {}
        answer = []
        
        # 입력된 파일 이름과 중복 횟수를 딕셔너리로 만들어줌
        for name in names:
            if name not in files.keys():
                files[name] = 1
            else:
                files[name] += 1
        
        # 파일 이름 생성
        for key in files.keys():
            # 파일 이름이 중복되지 않은 경우
            if files[key] == 1:
                answer.append(key)

            # 파일 이름이 2번 이상 중복된 경우
            else:
                answer.append(key)
                files[key] -= 1
                
                cnt = 0
                tmp = key + '(' + str(cnt) + ')'
                
                while files[key] > 0:
                    if tmp not in files.keys():
                        cnt += 1
                        files[key] -= 1
                        tmp = key + '(' + str(cnt) + ')' 
                    answer.append(tmp)
                    
        return answer
