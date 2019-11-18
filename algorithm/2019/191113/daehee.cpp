// Time Out

class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int height = matrix.size();
        int width = matrix[0].size();
        int answer = 0;
        
        for(int now_hei = 0; now_hei < height; now_hei++)
            for(int now_wid = 0; now_wid < width; now_wid++){
                for(int ob_hei = now_hei; ob_hei < height; ob_hei++)
                    for(int ob_wid = now_wid; ob_wid < width; ob_wid++){
                        int temp = 0;
                        for(int n_h = now_hei; n_h<= ob_hei; n_h++)
                            for(int n_w = now_wid; n_w <= ob_wid; n_w++){
                                temp += matrix[n_h][n_w];
                            }
                        if(temp == target) answer++;
                    }
            }
        
        return answer;
    }
};