class Solution:
    def simplifyPath(self, path: str) -> str:

        current = ['/']
        paths = path.split("/")

        for path in paths:
            # 현재 위치를 나타내는 명령어일 경우, 그냥 지나
            if path == '.':
                continue
            # 부모 directory를 가리키는 명령어일 경우
            elif path == '..':
                # 현재 경로에서 부모가 있으면 pop!
                if len(current) > 1:
                    current.pop()
                # 없으면 그냥 지나감
                else:
                    continue
            # 제거할 수 있는 경로가 아닌 경우 그냥 더해준다
            elif path != '':
                current.append('/'+path)

        if len(current) == 1:
            return '/'
        
        return "".join(current[1:])

