# 솔루션을 참고했기 때문에 리뷰 안해주셔도 괜찮습니다.

from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        j, li = 0, []  # 인덱스 j와 결과를 저장할 리스트 li 초기화

        processorTime.sort()  # 프로세서 사용 가능 시간을 오름차순으로 정렬
        tasks.sort(reverse=True)  # 태스크 실행 시간을 내림차순으로 정렬

        for i in range(len(processorTime)):
            li.append(processorTime[i] + tasks[j])  # 현재 프로세서에 할당된 태스크 실행 시간을 결과 리스트에 추가
            j += 4  # 다음 프로세서에 할당될 태스크로 이동

        return max(li)  # 결과 리스트에서 가장 큰 값이 최소 실행 시간
