class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        s = []
        for p in path:

            if p:
                if p == '..':
                    s = s[:-1]
                elif p != '.':
                    s.append(p)

        return '/' + '/'.join(s)
