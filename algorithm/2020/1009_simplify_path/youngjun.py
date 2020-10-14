class Solution(object):
    def simplifyPath(self, path):

        answer=""

        # "/"로 split한 요소들 추출
        elements=path.split(("/"))
        tmp=[]

        #split한 요소들을 돌면서 경로 판단해서 정답에 해당하는 디렉토리들 이름 추출
        for e in elements:
            if e=="." or e=="":
                continue
            elif e=="..":
                if tmp:
                    tmp.pop()
            else:
                tmp.append(e)

        #디렉토리 형태로 추출한 이름들 구성
        if not tmp:
            answer="/"
        else:
            for i in tmp:
                answer+="/"+i

        return answer

if __name__ == '__main__':
    input="/"
    s=Solution()
    print(s.simplifyPath(input))