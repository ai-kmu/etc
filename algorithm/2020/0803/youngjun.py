#7:15~ 8:05
# Add Two Numbers
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        digitCount=0 # 숫자에 자릿수 곱해주는 역할
        l1Sum=0
        l2Sum=0

        while l1.next: # l1 숫자 더하기

            l1Sum+=l1.val*10**digitCount
            digitCount += 1
            l1=l1.next
        l1Sum += l1.val * 10 ** digitCount

        digitCount=0

        while l2.next: # l2 숫자 더하기

            l2Sum+=l2.val*10**digitCount
            digitCount += 1
            l2=l2.next
        l2Sum += l2.val * 10 ** digitCount

        sum=str(l1Sum+l2Sum) # l1 l2 숫자 더하기
        #Ouput 노드 만들기
        currentNode=ListNode(int(sum[0]))
        for i in range(1,len(sum)): #
            currentNode=ListNode(sum[i],currentNode)

        return currentNode


