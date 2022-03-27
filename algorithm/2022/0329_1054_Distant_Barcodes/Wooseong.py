from collections import Counter
# Counter(list)
# 하면 list의 원소와 그 개수를
# Counter({원소:개수}) 형태로 반환한다


# Main idea
# = 한 칸 씩 띄어서 넣으면 겹칠 일이 없을 것
# - 제일 많은 애 중 하나를 0번부터 짝수번째에 넣고
# - 남은 것들을 순서대로 나머지 짝수번째 자리와 홀수번째에 넣는다
# ex) [1,1,1,1,2,2,2,3,3]
# ->  [1,_,1,_,1,_,1,_,_] = 1 네 개 채우고
# ->  [1,_,1,_,1,_,1,_,2] = 남은 짝수번째 자리에 마저 채우고
# ->  [1,2,1,2,1,3,1,3,2] = 홀수번째에 남은 것들 넣기
class Solution:
    def rearrangeBarcodes(self, barcode):
        n = len(barcode)

        cnt = Counter(barcode)
        answer = [0] * n      # 길이만큼 0으로 만들어둠
        sorted_code = []      # barcode를 같은 것끼리 모아둘 list

        max_freq_code = max(cnt, key=cnt.get)     # 제일 많이 나온 barcode
        sorted_code.extend([max_freq_code]*cnt[max_freq_code]) # 걔부터 list 앞에 넣고
        cnt[max_freq_code] = 0
        for i in cnt.keys():
            sorted_code.extend([i] * cnt[i])      # 모아서 extend

        iter_code = iter(sorted_code)       # iter로 만든 다음에
        # 짝수번째 삽입
        for i in range(0,n,2):
            answer[i] = next(iter_code)     # next로 하나씩 호출 가능
        # 홀수번째 삽입
        for i in range(1,n,2):
            answer[i] = next(iter_code)     # for문이 달라져도 순서대로 나온다!

        return answer
