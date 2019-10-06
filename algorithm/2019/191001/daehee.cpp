#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer(2);
    vector<int> que;
    int cases = operations.size();
    
    for(int i = 0; i < cases; i++){
        
        istringstream iss(operations[i]);
        string op;
        int num;
        iss >> op >> num;
        
        if(op == "I"){
            que.push_back(num);
            continue;
        } 
        if(que.size() == 0) continue;
        if(num == 1){
            que.erase(max_element(que.begin(), que.end()));
            continue;
        }
        que.erase(min_element(que.begin(), que.end()));
        
    }
    
    
    if(que.size() == 0){
        answer[0] = 0;
        answer[1] = 0;
    } else{
        answer[0] = *max_element(que.begin(), que.end());
        answer[1] = *min_element(que.begin(), que.end());
    }
    
    return answer;
}