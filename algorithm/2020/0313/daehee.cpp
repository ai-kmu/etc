#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days;
    for(int i = 0; i < progresses.size(); i++){
        int temp = 100-progresses[i];
        int moc = temp / speeds[i];
        if(temp % speeds[i] > 0){
            moc++;
        }
        days.push_back(moc);
    }
    if(days.size() == 1){
        answer.push_back(1);
        return answer;
    }
    int index = 0;
    int max = days[0];
    for(int i = 1; i < progresses.size(); i++){
        int day = 0;
        if(max < days[i]){
            for(int j = index; j < i; j++){
                day++;
            }
            answer.push_back(day);
            index = i;
            max = days[i];
        }
        if( i == progresses.size()-1 ){
            day = 0;
            for(int j = index; j < days.size(); j++){
                day++;
            }
            answer.push_back(day);
        }
    }
    return answer;
}
