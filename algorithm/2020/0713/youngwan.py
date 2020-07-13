from collections import deque

class Solution:
    def maxNumber(self, nums1, nums2, k):
        def check_len(n, nums1, nums2, k):
            for i in range(len(nums1)):
                num, now_n = nums1.popleft()
                if n < now_n:
                    nums1.append((num, now_n))
            if len(nums1) + len(nums2) < k - 2:
                return nums1, False
            else:
                return nums1, True
            
            
        n1 = 0
        n2 = 0
        answer = []
        if len(nums1) + len(nums2) == k:
            while len(nums1) != n1 and len(nums2) != n2:
                print(n1, nums1[n1], n2, nums2[n2])
                if nums1[n1] < nums2[n2]:
                    answer.append(nums2[n2])
                    n2 += 1
                elif nums1[n1] > nums2[n2]:
                    answer.append(nums1[n1])
                    n1 += 1
                else:
                    n11 = n1 + 1
                    n22 = n2 + 1
                    change = 0
                    while len(nums1) != n11 and len(nums2) != n22:
                        if nums1[n11] < nums2[n22]:
                            answer.append(nums2[n2])
                            n2 += 1
                            change = 1
                            break
                        elif nums1[n11] > nums2[n22]:
                            answer.append(nums1[n1])
                            n1 += 1
                            change = 1
                            break
                        else:
                            n11 += 1
                            n22 += 1
                    if change == 0:
                        answer.append(nums1[n1])
                        answer.append(nums2[n2])
                        n1 += 1
                        n2 += 1
            if len(nums1) == n1:
                while len(nums2) != n2:
                    answer.append(nums2[n2])
                    n2 += 1
            else:
                while len(nums1) != n1:
                    answer.append(nums1[n1])
                    n1 += 1
            return answer

        else:
            nums1_deq = []
            nums2_deq = []

            for i, num in enumerate(nums1):
                nums1_deq.append((num, i))
            for i, num in enumerate(nums2):
                nums2_deq.append((num, i))

            nums1_deq = deque(sorted(nums1_deq, reverse=True))
            nums2_deq = deque(sorted(nums2_deq, reverse=True))

            num1, n1 = nums1_deq.popleft()
            num2, n2 = nums2_deq.popleft()

            while nums1_deq and nums2_deq:
                if num1 < num2:
                    temp_nums_deq, temp_bool = check_len(n2, nums2_deq, nums1_deq, k)
                    if temp_bool:
                        answer.append(num2)
                        nums2_deq = temp_nums_deq
                        k -= 1
                    else:
                        nums2_deq.append((num2, n2))
                    if nums2_deq:
                        num2, n2 = nums2_deq.popleft()
                    else:
                        num2 = -1

                elif num1 > num2:
                    temp_nums_deq, temp_bool = check_len(n1, nums1_deq, nums2_deq, k)
                    if temp_bool:
                        answer.append(num1)
                        nums1_deq = temp_nums_deq
                        k -= 1
                    else:
                        nums1_deq.append((num1, n1))
                    if nums1_deq:
                        num1, n1 = nums1_deq.popleft()
                    else:
                        num1 = -1
                else:
                    break
            if nums1_deq:
                while k != 0:
                    if num1 > num2:
                        temp_nums_deq, temp_bool = check_len(n1, nums1_deq, nums2_deq, k)
                        if temp_bool:
                            answer.append(num1)
                            nums1_deq = temp_nums_deq
                            k -= 1
                        else:
                            nums1_deq.append((num1, n1))
                        if nums1_deq:
                            num1, n1 = nums1_deq.popleft()
                        else:
                            num1 = -1
                    elif num1 < num2:
                        answer.append(num2)
                        k -= 1
                        num2 = -1
                    else:
                        if k >= 2:
                            answer.append(num1)
                            answer.append(num2)
                            k -= 2
                            num2 = -1
                        else:
                            answer.append(num1)
                            k -= 1
            else:
                while k != 0:
                    if num1 < num2:
                        temp_nums_deq, temp_bool = check_len(n2, nums2_deq, nums1_deq, k)
                        if temp_bool:
                            answer.append(num2)
                            nums2_deq = temp_nums_deq
                            k -= 1
                        else:
                            nums2_deq.append((num2, n2))
                        if nums2_deq:
                            num2, n2 = nums2_deq.popleft()
                        else:
                            num2 = -1
                    elif num1 > num2:
                        answer.append(num1)
                        k -= 1
                        num1 = -1
                    else:
                        if k >= 2:
                            answer.append(num1)
                            answer.append(num2)
                            k -= 2
                            num1 = -1
                        else:
                            answer.append(num1)
                            k -= 1
        return answer
