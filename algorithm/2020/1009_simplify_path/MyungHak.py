# split 한 후에 .이거나 길이가 0이면 무시 그리고 ..이면 뒤로 한칸 가게 만든다

class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        OptPathArr = []
        for p in paths:
            if len(p) == 0:
                pass
            elif p == ".":
                pass
            elif p == "..":
                OptPathArr = OptPathArr[:-1]
            else:
                OptPathArr.append(p)
        OptPath = ""
        for p in OptPathArr:
            OptPath += "/" + p
        if len(OptPath) == 0:
            OptPath = "/"
        return OptPath
