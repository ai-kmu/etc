class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        
        
        answer = len(barcodes) * [0]
        cur_point = 0
        
        # counter를 이용하여 개수가 많은 수부터 처리
    
        barcode_inorder = Counter(barcodes).most_common()
        
        # 2칸씩 띄어가며 수(count)가 많은 수(num)부터 answer에 추가
        # 범위를 넘어서면 처음부터 값 추가
        # 이미 채워진 칸을 만나면 cur_point에 +1 하여 진행
        
        for num, count in barcode_inorder:
            for i in range(count):
                if cur_point > len(answer) - 1:
                    cur_point = 0

                while answer[cur_point] != 0:
                    cur_point += 1

                answer[cur_point] = num
                cur_point += 2

        return answer
