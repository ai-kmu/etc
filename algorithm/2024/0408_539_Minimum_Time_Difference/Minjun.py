class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 최대값보다 큰 값 설정
        tmp = 24*60 + 1
        trans = []
        # 분으로 전환
        for _ in timePoints:
            h, m = _.split(":")
            trans.append(int(h) * 60 + int(m))
        # 정렬 및 요소 간 최소 차이 구함
        trans.sort()
        for i in range(len(trans)-1):
            tmp = min(tmp, abs(trans[i+1] - trans[i]))
        # 24:00에서 순환하므로 처음과 끝 고려.
        tmp = min(tmp, abs(24 * 60 - (trans[-1] - trans[0])))
        return tmp
   
