# 기본 알고리즘
# 1. matrix에 있는 0과 1은 사실 그 요소를 오른쪽 아래 끝으로 하는 maximul square size의 최솟값
#    kl_mat을 새로 만들어서, 그 요소를 오른쪽 아래 끝으로 하는 maximul square size를 [i][j]에 저장
# 2. kl_mat의 1행과 1열 각각은 matrix와 동일
# 3. kl_mat[i][j] (d) = min(kl_mat[i-1][j-1] (a), kl_mat[i][j-1](b), kl_mat[i-1][j](c)) + 
#    => a,b,c가 모두 1이면 d까지 크기 2에서 1을 가짐 -> 2로 변환
#    => 하나라도 0이면 d를 오른쪽 아래 끝으로 하는 maximul square size는 1 -> min(~,~,0) +1 = 1
#    => 모두 2이면, d를 오른쪽 아래 끝으로 하는 maximul square size는 3이 된다.



class Solution:
    def maximalSquare(self, matrix):
        # 주어진 matrix 크기
        m = len(matrix)     # 행 개수
        n = len(matrix[0])  # 열 개수

        # str을 int로 변형
        matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
    
        ### 코드 의미: 행과 열 둘 중에 하나가 1일 경우 => 행(열) 벡터의 합이 0이면 ㅇ반환, 1이면 1반환
        ### feedback: 연산을 빠르게 끝나기 위해서 코드 추가 (없어도 돌아감)
    
        # 행이나 열이 1일 경우
        # 1이 하나라도 있으면 답은 1**2 = 1,
        # 하나도 없으면 답은 0
        if (m == 1) | (n == 1):
            for i in matrix:
                if sum(i): return 1   # 각 행의 sum이 1이상 (true)이면 1이 있음
            return 0                  # 모든 행의 sum이 false처리되면 (0이면) 1이 없음

        # matrix에서 해당 요소를 오른쪽 아래 끝으로 하는 maximul kernel length(kl) 값을
        # 요소로 갖는 행렬 :  1행과 1열은 matrix와 동일, 나머지는 0으로 할당
        
        ### feeback: flattne 방식 대신해서 이중 for문내에서 갱신
        # result = 0 => (최초의 값) 
        
        kl_mat = [[matrix[i][j] if i*j == 0 else 0 for j in range(n)] for i in range(m)]
        # result = max(max(kl_mat)) => 첫번쨰 행과 열중의 1값이 있는지 여부(1 * 1
        
        for i in range(1,m):
            for j in range(1,n):
                # matrix의 요소가 1일 때만 업데이트: 0이면 그대로 0으로 두어야함
                if matrix[i][j] == 1:
                    kl_mat[i][j] = min(kl_mat[i-1][j-1], kl_mat[i][j-1], kl_mat[i-1][j]) + 1
                
                # result = max(result, kl_mat[i][j]) => 탐색하면서 갱신
                    
        # 이건 사실 max(max(kl_mat))랑 max(map(max,kl_mat))을 해봤는데 => feedback: 행 list끼리 max값을 비교(첫번재 요소 비교 -> 두번째 요소 비교)  
        # 의도한 대로 나오지 않아서 만든 임시방편입니다.
        
        ## 데이터를 Flatten 하는 것도 좋지만 / 앞선 탐색과정에서 동시에 처리하는 게 조금 더 시간 측면에서 효율적임
        flatten = [kl_mat[i][j] for i in range(m) for j in range(n)]

        return max(flatten) ** 2
