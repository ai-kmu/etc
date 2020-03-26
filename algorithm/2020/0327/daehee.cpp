#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(string arrangement) {
    int answer = 0;
    stack<int> s;
    
    bool ex = false;       // condition
    for(int i = 0; i<arrangement.length(); i++){
        if(arrangement.at(i) == '('){   // 여는 괄호인 경우
            s.push(1);     // 열린괄호 수 체크
            ex = false;    // 열린상태 표시
            continue;      
        }
        if(arrangement.at(i) == ')'){   // 닫힌 괄호인 경우
            s.pop();          // 열린괄호 하나 제거
            if(ex == true){   // 이전 괄호가 닫힌괄호
                answer++;     
                ex = true;
                continue;
            }
                                // 이전 괄호가 열린괄호
            answer += s.size(); // 겹친 것들 더하기
            ex = true;
            continue;
        }
    }
    return answer;
}
