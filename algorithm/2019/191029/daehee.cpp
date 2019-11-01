#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;
    
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    
    int check = 0;
    for(int i = 0; i < A.size(); i++){
        for(int j = check; j < A.size(); j++){
            if(A.at(i) < B.at(j)){
                answer++;
                check = j+1;
                break;
            }
        }
    }
    
    return answer;
}