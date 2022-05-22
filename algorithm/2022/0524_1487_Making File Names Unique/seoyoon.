# 참고한 풀이
class Solution:
    def getFolderNames(self, names):
        m = dict()
        l = list() # 결과저장용 리스트 

        for name in names: # 각각의 이름을 순환하면서
            new_file_name = name
            last_file_id = 0
            if (m.get(name) != None): # 만약 이름이 이미 생성됐으면
                last_file_id = m[name]+1 # 하나 더함
                while (True): # ["onepiece","onepiece(1)"] 이런 사례를 제어하기 위함
                    new_file_name = "{}({})".format(name,last_file_id)
                    if (m.get(new_file_name) == None): break
                    else: last_file_id+=1
            m[name] = last_file_id
            if (new_file_name != name): m[new_file_name]=0 # onepiece(1)를 사전에 추가
            l.append(new_file_name) # new_file_name을 리스트에 추가
        return l
