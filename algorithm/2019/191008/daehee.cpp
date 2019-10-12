#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool check[100001];
int maxim;


bool dfs(string departure, vector<vector<string>> &tickets, vector<string> &answer){
    answer.push_back(departure);
    if(answer.size() == maxim){
        return true;
    }
    
    for(int i = 0; i <tickets.size(); i++){
        if(answer.back() == tickets[i][0]){
            if(check[i] == false){
                check[i] = true;
                dfs(tickets[i][1], tickets, answer);
                check[i] = false;
                if(answer.size()== maxim) return true;
            }
        }
    }
    answer.pop_back();
    return false;
}



vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    sort(tickets.begin(),tickets.end());
    maxim = tickets.size()+1;
    
    for(int i = 0 ; i <tickets.size(); i++){
        if(tickets[i][0] == "ICN"){
            check[i] = true;
            answer.push_back(tickets[i][0]);
            bool a = dfs(tickets[i][1], tickets, answer);
            if(a) break;
            answer.pop_back();
            check[i] = false;
        }
    }
    
    
    return answer;
}