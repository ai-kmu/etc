class Solution(object):
    def getPermutation(self, n, k):
        
        # 사용할 수 list를 만들고 사용한수를 빼가면서진행
        # 그 수를 사용했을때 몇변째 수에 해당하는지 순열의 수로 계산
        # k번째수를 넘어가지않는 최대 수를 구하고, 넘어가면 다음 자릿수로 이동
        
        # 사용할 수 리스트
        num_list = [ x+1 for x in range(n)]
        
        # k번째 수와 비교할 수
        compare_num = 0
        
        # list의 몇번째 수를 사용할것인지를 표시
        list_num_count = 0
        answer = ''
        
        # n번째 자릿수에서 1번째 자릿수까지 순으로 사용할수를 정함 
        for place_value in range(n-1, 0, -1):
            # n번째 자리에서 k번째수를 넘어가지않는 최대 수를 구하고, 넘어가면 다음 자릿수로 이동
            while True:
                if k > math.factorial(place_value) + compare_num:
                    list_num_count += 1
                    compare_num += math.factorial(place_value)
                # 조건을 만족하면 answer에 찾은 수를 추가, list_num_count에서 사용한 수 pop ,변수 초기화
                else:
                    answer += str(num_list[list_num_count])
                    num_list.pop(list_num_count)
                    list_num_count = 0
                    break
                    
        return answer + str(num_list[0])
