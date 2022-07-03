//실패
//시간초과
class Solution {
public:
    int rob(vector<int>& nums) {//훔치기
        int max = 0;
        int size = nums.size() / 2;
        if (!size) size = 1;
        max = robByTime(size, nums, 1);//훔치는 횟수에 따른 재귀함수로 풀이
        return max;
    }

    //훔치는 횟수에 따른 최댓값, 재귀
    int robByTime(int num, vector<int> vec, int init) {
        if (num == 0) return 0; //재귀 종료 조건
        int select = 0; //값 저장
        int max = 0; //리턴값
        vector<int>::iterator iter;//반복자
        for (int i = 0; i < vec.size(); i++) {
            iter = vec.begin(); //반복자를 받아서
            iter += i; //시작점을 옮긴 뒤
            select = *iter; //값을 저장
            if(iter != vec.end()) iter = ++iter == vec.end() ? vec.end() : ++iter; //iter를 두 칸 이동시킨다.
            if (init && i == 0) { if (iter == vec.end()){ iter--; } select += robByTime(num - 1, vector<int>(iter, vec.end() - 1), 0); } //원형 지형을 고려, 처음 시작때를 고려한다.
            else select += robByTime(num - 1, vector<int>(iter, vec.end()), 0); //시작점에서 2칸 떨어진 vec로 재귀 호출, 값을 더함
            if (select > max) max = select; //max값 검증
        }
        return max;
    }
};
