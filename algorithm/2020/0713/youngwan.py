from collections import deque
import copy

class Solution:
    def maxNumber(self, nums1, nums2, k):
        def check_len(n, nums1, nums2, k, last_num=0):
            for i in range(len(nums1)):
                num, now_n = nums1.popleft()
                if n < now_n:
                    nums1.append((num, now_n))
            if last_num == -1:
                if len(nums1) + len(nums2) < k - 1:
                    return nums1, False
                else:
                    return nums1, True
            else:
                if len(nums1) + len(nums2) < k - 2:
                    return nums1, False
                else:
                    return nums1, True


        def check_min(nums1, nums2):
            while nums1 and nums2:
                num1, n1 = nums1.popleft()
                num2, n2 = nums2.popleft()
                if num1 < num2:
                    return 0
                elif num1 > num2:
                    return 1
            if not nums1:
                return 0
            else:
                return 1
            
            
        n1 = 0
        n2 = 0
        answer = []
        if len(nums1) + len(nums2) == k:
            while len(nums1) != n1 and len(nums2) != n2:
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
                        if len(nums1) == n11:
                            if nums1[n1] < nums2[n2+1]:
                                answer.append(nums2[n2])
                                n2 += 1
                            else:
                                answer.append(nums1[n1])
                                n1 += 1
                        else:
                            if nums1[n1+1] > nums2[n2]:
                                answer.append(nums1[n1])
                                n1 += 1
                            else:
                                answer.append(nums2[n2])
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

            nums1_deq = deque(sorted(nums1_deq, key = lambda x : (-x[0], x[1])))
            nums2_deq = deque(sorted(nums2_deq, key = lambda x : (-x[0], x[1])))

            print(nums1_deq, nums2_deq)

            num1, n1 = nums1_deq.popleft()
            num2, n2 = nums2_deq.popleft()

            while nums1_deq and nums2_deq:
                print(n1, num1, n2, num2)
                print(nums1_deq, nums2_deq)
                if num1 < num2:
                    temp_nums2 = copy.deepcopy(nums2_deq)
                    temp_nums_deq, temp_bool = check_len(n2, temp_nums2, nums1_deq, k)
                    if temp_bool:
                        answer.append(num2)
                        nums2_deq = temp_nums_deq
                        k -= 1
                    else:
                        nums2_deq.append((num2, n2))
                    if nums2_deq:
                        num2, n2 = nums2_deq.popleft()
                        nums2_deq = deque(sorted(list(nums2_deq), reverse=True))
                    else:
                        num2 = -1

                elif num1 > num2:
                    temp_nums1 = copy.deepcopy(nums1_deq)
                    temp_nums_deq, temp_bool = check_len(n1, temp_nums1, nums2_deq, k)
                    if temp_bool:
                        answer.append(num1)
                        nums1_deq = temp_nums_deq
                        k -= 1
                    else:
                        nums1_deq.append((num1, n1))
                    if nums1_deq:
                        num1, n1 = nums1_deq.popleft()
                        nums1_deq = deque(sorted(list(nums1_deq), reverse=True))
                    else:
                        num1 = -1
                else:
                    temp_nums1 = copy.deepcopy(nums1_deq)
                    temp_nums2 = copy.deepcopy(nums2_deq)
                    min_nums = check_min(temp_nums1, temp_nums2)
                    if min_nums == 0:
                        temp_nums1 = copy.deepcopy(nums1_deq)
                        temp_nums_deq, temp_bool = check_len(n1, temp_nums1, nums2_deq, k)
                        if temp_bool:
                            answer.append(num1)
                            nums1_deq = temp_nums_deq
                            k -= 1
                        else:
                            nums1_deq.append((num1, n1))
                        if nums1_deq:
                            num1, n1 = nums1_deq.popleft()
                            nums1_deq = deque(sorted(list(nums1_deq), reverse=True))
                        else:
                            num1 = -1
                    else:
                        temp_nums2 = copy.deepcopy(nums2_deq)
                        temp_nums_deq, temp_bool = check_len(n2, temp_nums2, nums1_deq, k)
                        if temp_bool:
                            answer.append(num2)
                            nums2_deq = temp_nums_deq
                            k -= 1
                        else:
                            nums2_deq.append((num2, n2))
                        if nums2_deq:
                            num2, n2 = nums2_deq.popleft()
                            nums2_deq = deque(sorted(list(nums2_deq), reverse=True))
                        else:
                            num2 = -1
            print(answer, nums1_deq, nums2_deq, num1, num2)
            if nums1_deq:
                while k != 0:
                    if num1 > num2:
                        temp_nums1 = copy.deepcopy(nums1_deq)
                        temp_nums_deq, temp_bool = check_len(n1, temp_nums1, nums2_deq, k, num2)
                        if temp_bool:
                            answer.append(num1)
                            nums1_deq = temp_nums_deq
                            k -= 1
                        else:
                            nums1_deq.append((num1, n1))
                        if nums1_deq:
                            num1, n1 = nums1_deq.popleft()
                            nums1_deq = deque(sorted(list(nums1_deq), reverse=True))
                        else:
                            num1 = -1
                    else:
                        answer.append(num2)
                        k -= 1
                        num2 = -1
            else:
                while k != 0:
                    if num1 < num2:
                        temp_nums2 = copy.deepcopy(nums2_deq)
                        temp_nums_deq, temp_bool = check_len(n2, temp_nums2, nums1_deq, k, num1)
                        print(temp_bool)
                        if temp_bool:
                            answer.append(num2)
                            nums2_deq = temp_nums_deq
                            k -= 1
                        else:
                            nums2_deq.append((num2, n2))
                        if nums2_deq:
                            num2, n2 = nums2_deq.popleft()
                            nums2_deq = deque(sorted(list(nums2_deq), reverse=True))
                        else:
                            num2 = -1
                    else:
                        answer.append(num1)
                        k -= 1
                        num1 = -1
        return answer
