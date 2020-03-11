#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> times, returns;
    int currentMax, returnsNum = 0;
    returns.push_back(0);
   
    for ( int i = 0; i < progresses.size(); i++) {
        
        times.push_back( (100-progresses[i])/speeds[i] + ((100-progresses[i])%speeds[i] ? 1: 0) );
        
        if ( i == 0 )   currentMax = times[0];
        
        if( i != 0 && times[i] > currentMax) {
            currentMax = times[i];
            returnsNum++;
            returns.push_back(1);
        }
        else {
            returns[returnsNum]++;  
        }
    } 
    return returns; 
}
