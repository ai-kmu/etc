#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

string solution(int n, int t, int m, vector<string> timetable) {
    string answer = "";
    # timetable의 시각은 순서대로 주어지지 않기 때문에 우선순위 큐를 사용했다.
    priority_queue<int, vector<int>, greater<int>> times;
    int hour, minute;
    
    // timetable에 입력된 HH:MM 형태의 시간에서 각각 시, 분을 구해서 time 큐에 집어넣는다.
    for(int i=0; i<timetable.size(); i++){
        hour = (timetable[i][0] - '0')*10 + timetable[i][1]-'0';
        minute = (timetable[i][3]-'0')*10 + timetable[i][4]-'0';
        times.push(hour*60 + minute);
    }
    
    // 셔틀버스는 09:00 부터 출발하므로, 셔틀버스 출발 시각을 9*60으로 초기화해준다.
    int start, cnt = 0, result, last;
    start = 9*60;
    
    
    // 콘은 가능한 가장 늦은 셔틀버스를 타고 싶기 때문에 n-1번째 셔틀까지는 m명 이내의 승객을 태울 수 있도록 했다.
    for(int i=0; i < n-1; i++){
        start = 9*60 + i*t;
        cnt = 0;
        
        while(!times.empty() && cnt < m ){
            if(times.top() <= start){ //지금 셔틀을 탈 수 있다면
                times.pop();
                cnt++;
            }
            else
                break;
        }
    }
  
    /*
    마지막 셔틀은 m-1 번째까지 태웠을 때 두가지 경우가 있다.
    m-1번째 태운 크루외 도착시각과 그 다음 기다리는 크루의 도착시각이 같다면 콘은 m-1번째 승객보다 1분 빨리 도착해야한다.
    두번째는 m-1번째 태운 크루의 도착시각이 마지막 셔틀버스의 출발시각보다 늦으면 콘은 해당 셔틀버스 출발시각에 도착해도 된다.
    */
    cnt = 0;
    start = 9*60 + t*(n-1); 
    while(!times.empty() && cnt < m-1 ){
        if(times.top() <= start){
            times.pop();
            cnt++;
        }
        else
            break;
    }
     
     
    if(times.empty() || times.top() > start ){
        result = start;
    }
    else{
        result = times.top()-1;
    }

    hour = result/60;
    minute = result%60;
             
    // 아래는 출력 포맷을 맞춰주는 부분
    answer += hour/10 + '0';     
    answer += hour%10 + '0';
    answer += ':';
    answer += minute/10 + '0';      
    answer += minute%10 + '0';
    
    return answer;
}
