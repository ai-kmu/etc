# 현재 파일이 지금까지 나왔는지 확인
# 없으면 그냥 추가
# 있으면 다음 알고리즘 실행
#     현재 그 이름이 몇개 나왔는지 저장해둔 container에서 가져옴
#     그 숫자부터 시작해서 1씩 늘려가며 중복되는 이름이 있는지 확인
#     없으면 그 숫자를 저장하고 종료


class Solution:
    def getFolderNames(self, names):
        ans, container = [], {}
        for i, name in enumerate(names):
            count= 0
            name_origin = name
            
            if name in container:
                count = container[name]
                while(name in container):
                    count+=1
                    name = f"{name_origin}({count})"
                    
                name = f"{name_origin}({count})"
            
            if name != name_origin:
                container[name] = 0  
            else:
                container[name] = count
            
            ans.append(name)
        return ans
