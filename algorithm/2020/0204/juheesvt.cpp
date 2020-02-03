#include <iostream>

using namespace std;

const int maxWidth = 101;
const int maxHeight = 101;
int main(){
    int mapp[maxWidth][maxHeight]={0,};
    int N;
    scanf("%d",&N);
    int sum[101]={0,};
    for(int c = 1; c<=N;++c){
        int x,y,width,height;
        scanf("%d %d %d %d",&x,&y,&width,&height);
        for(int i =0;i<maxHeight;++i){
            for(int j = 0; j<maxWidth;++j){
                if(j>=x && j < x+width && i >= y && i < y+height){
                    if(mapp[i][j] != 0){
                        sum[mapp[i][j]]-=1;
                    }
                    sum[c] += 1;
                    mapp[i][j] = c;
                }
            }
        }
    }
    for(int i = 1;i<=N;++i){
        printf("%d\n",sum[i]);
    }
    return 0;
}
