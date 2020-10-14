class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        real_paths=[]
        for path in paths:                      # 경로들 걸러내기
            if path=='' or path=='.':           # 현재위치 그대로
                continue
            elif path=='..':                    # 상위 디렉토리
                if len(real_paths)>=1:
                    del real_paths[-1]
            else:                               # 하위 디렉토리
                real_paths.append(path)
            
        real_path = '/'
        for i, path in enumerate(real_paths):   # 값 재조합
            if i>0:
                real_path += '/'
            real_path += path

        return real_path
        
