#56. Merge Intervals
#12:08~

class Solution(object):
    def merge(self, intervals):

        intervals.sort()
        if len(intervals)<2:
            return intervals

        answer=[]
        interval_candidate=intervals[0]
        for interval in intervals:
            if interval[0]>interval_candidate[1]:
                answer.append(interval_candidate)
                interval_candidate=interval
            else:
                interval_candidate[1]=max(interval_candidate[1],interval[1])

        answer.append(interval_candidate)
        return answer


if __name__ == '__main__':
    s=Solution()
    intervals=[[15,18],[1,3],[2,6],[8,10]]
    print(s.merge(intervals))
