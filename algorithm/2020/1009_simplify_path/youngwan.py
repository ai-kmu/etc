class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.strip().split('/')                # /를 기준으로 list 반환
        c_path_list = []
        for i in path_list:
            if ( i == '..'):                               
                if len(c_path_list) != 0:
                    del c_path_list[len(c_path_list)-1]    # '..'이고 앞에 path가 있는 경우 바로 앞 path 삭제
            elif i == '.' or i == '':                      # '.' 또는 ''는 무시
                continue 
            else:                       
                c_path_list.append(i)                      # path인 경우 list에 추가
        if c_path_list:                                    # path가 있는 경우
            c_path = ""
            for i in c_path_list:                          # /path 형식으로 더하여 반환
                c_path += "/"
                c_path += i
            return c_path
        else:
            return "/"                                     # path가 없는 경우 "/" 반환
