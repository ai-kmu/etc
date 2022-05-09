class Solution:
    # 다음과 같은 triangle tree를 만드는 것이 목적이다.
    '''
      1                   1
     1 2=============>   2 3
    1 2 3               3 4 6
    
    삼각형의 각 열에는 윗 열로부터 최솟값을 누적하여 기록하게 된다.
    최종적으로 가장 밑 열의 요소 중 최소값을 가지는 요소가 minimum path가 되게 된다.
    여기서는 cache라는 개념을 도입하여 전체 누적 triangle tree를 만드는 대신 어떤 열의 요소를 만들 때 위의 열만 cache로 저장하게 하였다.
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache_row = None # 처음에는 cache_row를 None객체로 생성한다.
        for row in triangle: # 삼각형의 각 열을 순환하면서
            tmp_row = [] # 해당 열의 누적값을 기록할 빈 리스트를 만든다.
            for index, target in enumerate(row): # 열의 각 요소를 순환하면서
                if cache_row == None: # 첫번째 열이라면 누적값을 만들 필요가 없다.
                    tmp_row.append(target)
                else: # 두번째 열부터는 누적값을 선택하여 기록한다.
                    if index == 0: # 첫 요소에 대해서는 하나의 선택지만 존재한다.
                        tmp_row.append(target + cache_row[0])
                    elif index == len(row) - 1: # 마지막 요소에 대해서도 하나의 선택지만 존재한다.
                        tmp_row.append(target + cache_row[len(cache_row)-1])
                    else: # 중간에 있는 요소에 대해서는 윗열에서 자신의 왼쪽에 있는 요소를 택할지 
                          # 오른쪽에 있는 요소를 택할지 선택할 수 있다.
                        tmp_row.append(target + min(cache_row[index - 1], cache_row[index])) # 최솟값을 기록한다.
            cache_row = tmp_row # 해당열을 cache로 저장하여 밑의 열을 만들 때 사용이 가능하도록 한다.
        return min(tmp_row) # 가장 밑에 있는 열의 최솟값을 리턴한다.
