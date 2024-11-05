class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        # answer을 위한 0 list
        aws = []
        for i in range(k):
            aws.append(0)

        # log 중복 제거, users_UAM을 위한 dic 선언
        logs_set = set()
        users_UAM = dict()
        for i in logs:
            logs_set.add(tuple(i))
            users_UAM[i[0]] = 0
        
        # UAM 계산
        for i in logs_set:
            users_UAM[i[0]] += 1

        # answer에 반영
        for i in users_UAM.values():
            aws[i-1] += 1
        return aws
