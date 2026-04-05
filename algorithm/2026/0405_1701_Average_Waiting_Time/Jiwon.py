class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cnt = len(customers)
        curr = sum(customers[0])
        waiting = curr - customers[0][0]
        customers.pop(0)

        for customer in customers:
            if customer[0] >= curr:
                curr = sum(customer)
                waiting += customer[1]
            else:
                curr += customer[1]
                waiting += curr - customer[0]

        return waiting/cnt
