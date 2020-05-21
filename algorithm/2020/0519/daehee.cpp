#include <string>
#include <vector>

using namespace std;

int n1[5] = {1,2,3,4,5};                 // 순서 하드코딩
int n2[8] = {2,1,2,3,2,4,2,5};
int n3[10] = {3,3,1,1,2,2,4,4,5,5};

int max(int a, int b){                  // 최댓값 리턴
    return a < b ? b : a;
}

vector<int> solution(vector<int> answers) {
    int value = 0;
    vector<int> answer;
    vector<int> count(3);                      

    for(int i = 0; i < answers.size() ; i++){           // count 세기
        if(n1[i % 5] == answers[i]) count[0]++;
        if(n2[i % 8] == answers[i]) count[1]++;
        if(n3[i % 10] == answers[i]) count[2]++;
    }

    value = max(max(count[0],count[1]),count[2]);

    for(int i = 0; i < 3; i++)
        if(count[i] == value) answer.push_back(i+1);    // 맞으면 푸쉬

    return answer;
}
