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
