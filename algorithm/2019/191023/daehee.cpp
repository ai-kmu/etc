#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int memo[501][501];


int dp(int height, int index, vector<vector<int>> &triangle){
    if(memo[height][index] > 0){
        return memo[height][index];
    }
    
    if(index == 0){
        if(memo[height][index] < dp(height-1, index, triangle) + triangle[height][index]){
            memo[height][index] = dp(height-1, index, triangle) + triangle[height][index];
        }
        return memo[height][index];
    } else if(index == height){
        if(memo[height][index] < dp(height-1, index-1, triangle) + triangle[height][index]){
            memo[height][index] = dp(height-1, index-1, triangle) + triangle[height][index];
        }
        return memo[height][index];
    }
  
    
    int bigger = max(dp(height-1,index-1, triangle), dp(height-1,index, triangle));
    if(memo[height][index] < bigger + triangle[height][index]){
        memo[height][index] = bigger + triangle[height][index];
    }
    return memo[height][index];
}



int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int height = triangle.size();
    memo[0][0] = triangle[0][0];
    
    
    for(int i = 0; i < height; i++){
        dp(height-1, i, triangle);
    }
    answer = *max_element(&memo[height-1][0], &memo[height-1][height-1]);
    
    return answer;
}