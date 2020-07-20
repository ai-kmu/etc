# Create Maximum Number
주소 : https://leetcode.com/problems/create-maximum-number/

두 개의 리스트와 k가 주어지면 길이가 k인 가장 큰 숫자를 만드는 문제

## 조건. 두 개의 리스트의 순서는 유지되어야한다.  
예) nums1 = [8, 5, 1], nums2 = [9, 6, 7 ], k=4인 경우  
[9, 8, 7, 5] -> 가능  
[9, 8, 7, 6] -> 불가능  

### 예시1  
Input:  
nums1 = [3, 4, 6, 5]  
nums2 = [9, 1, 2, 5, 8, 3]  
k = 5  
Output:  
[9, 8, 6, 5, 3]  

### 예시2  
Input:  
nums1 = [6, 7]  
nums2 = [6, 0, 4]  
k = 5  
Output:  
[6, 7, 6, 0, 4]  

### 예시3  
Input:  
nums1 = [3, 9]  
nums2 = [8, 9]  
k = 3  
Output:  
[9, 8, 9]  






## 제가 푼 풀이  
1. k == len(nums1) + len(nums2)인 경우  
버려지는 숫자가 없기 때문에 앞에서부터 순서대로 비교하여 큰 것부터 정답에 넣어주면 됩니다  

예시)  
Input:  
nums1 = [6, 7]  
nums2 = [6, 0, 4]  
k = 5  

num1=6 num2=6 -> 다음 숫자가 큰 것을 먼저 추가 ( 7과 0이기 때문에 nums1의 6을 추가) answer = [6]   
num1=7 num2=6 -> 7 추가 answer = [6, 7] ( nums1이 비었기 때문에 num1=-1로 저장)  
num1=-1 num2=6 -> 6추가 answer = [6, 7, 6]  
num1=-1 num2=0 -> 0추가 answer = [6, 7, 6, 0]  
num1=-1 num2=4 -> 4추가 answer = [6, 7, 6, 0, 4]  


2. k < len(nums1) + len(nums2)인 경우  

예시)
Input:  
nums1 = [3, 4, 6, 5]  
nums2 = [9, 1, 2, 5, 8, 3]  
k = 5  

먼저 nums1과 nums2를 (숫자, 위치) 순으로 deque에 넣어주고 내림차순 정렬하여 줍니다  
nums1_deq = deque([(6,2), (5,3), (4,1), (3,0)])  
nums2_deq = deque([(9,0), (8,4), (5,3), (3,5), (2,2), (1,1)])  

num1 = 6, n1 = 2, num2 = 9, n2 = 0 -> answer = [9], k = 4
nums1_deq = deque([(5,3), (4,1), (3,0)])  
nums2_deq = deque([(8,4), (5,3), (3,5), (2,2), (1,1)])  

num1 = 6, n1 = 2, num2 = 8, n2 = 4  
8을 넣기 전에 8의 위치 4(n2)보다 낮은 위치의 번호들을 지운 뒤  
nums1_deq = deque([(5,3), (4,1), (3,0)])  
nums2_deq = deque([(3,5)])  
k - 2 <= len(nums1_deq) + len(nums2_deq)가 성립 -> answer = [9, 8], k = 3  
( k - 2를 하는 이유는 num1과 num2에 현재 저장된 값이 answer에 들어갈 수 있기 때문이고 위 식이 성립하지 않으면 k개를 뽑을 수 없다 )   

num1 = 6, n1 = 2, num2 = 3, n2 = 5 
nums1_deq = deque([(5,3)])  
nums2_deq = deque([])  
k - 2 <= 1(len(nums1_deq) + len(nums2_deq)) 성립 -> answer = [9, 8, 6], k = 2  

만약 nums1 = [3, 4, 5, 6]이었다면  
len(nums1_deq) + len(nums2_deq) = 0이 되기 때문에 answer에 추가할 수 없음  
이런 경우에는 nums1_deq에 다시 (num1, n1)을 추가 -> nums1_deq = deque([(5,2), (4,1), (3,0), (6,3)]  
num1 = 5, n1 = 2로 뽑고 nums1_deq를 다시 sort -> nums1_deq = deque([(6,3), (4,1), (3,0)])  

num1 = 5, n1 = 2, num2 = 3, n2 = 5  
nums1_deq = deque([])  
nums2_deq = deque([])  
answer = [9, 8, 6, 5], k = 1  
nums1_deq가 비었기 때문에 num1 = -1  

num1 = -1, n1 = 2, num2 = 3, n2 = 5  
nums1_deq = deque([])  
nums2_deq = deque([])  
answer = [9, 8, 6, 5, 3], k = 0  
