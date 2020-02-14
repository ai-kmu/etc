#include <iostream>
#include <algorithm>
using namespace std;
 
int red[3][1001];
int green[3][1001];
int blue[3][1001];
int r[1001]; int g[1001]; int b[1001];
int main()
{
    int n; scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d%d%d", &r[i], &g[i], &b[i]);
    }
    // 0: red, 1 : green, 2 : blue
    red[0][1] = r[1];
    red[1][2] = r[1] + g[2]; red[2][2] = r[1] + b[2]; red[0][2] = 9999;
    for (int i = 3; i < n; i++) {
        red[0][i] = min(red[1][i - 1], red[2][i - 1]) + r[i];
        red[1][i] = min(red[0][i - 1], red[2][i - 1]) + g[i];
        red[2][i] = min(red[0][i - 1], red[1][i - 1]) + b[i];
    }
    red[1][n] = min(red[0][n - 1], red[2][n - 1]) + g[n];
    red[2][n] = min(red[0][n - 1], red[1][n - 1]) + b[n];
    int min_red = min(red[1][n], red[2][n]);
 
    //green
    green[1][1] = g[1];
    green[0][2] = g[1] + r[2]; green[2][2] = g[1] + b[2]; green[1][2] = 9999;
    for (int i = 3; i < n; i++) {
        green[0][i] = min(green[1][i - 1], green[2][i - 1]) + r[i];
        green[1][i] = min(green[0][i - 1], green[2][i - 1]) + g[i];
        green[2][i] = min(green[0][i - 1], green[1][i - 1]) + b[i];
    }
    green[0][n] = min(green[1][n - 1], green[2][n - 1]) + r[n];
    green[2][n] = min(green[0][n - 1], green[1][n - 1]) + b[n];
    int min_green = min(green[0][n], green[2][n]);
 
    //blue
    blue[2][1] = b[1];
    blue[0][2] = b[1] + r[2]; blue[1][2] = b[1] + g[2]; blue[2][2] = 9999;
    for (int i = 3; i < n; i++) {
        blue[0][i] = min(blue[1][i - 1], blue[2][i - 1]) + r[i];
        blue[1][i] = min(blue[0][i - 1], blue[2][i - 1]) + g[i];
        blue[2][i] = min(blue[0][i - 1], blue[1][i - 1]) + b[i];
    }
    blue[0][n] = min(blue[1][n - 1], blue[2][n - 1]) + r[n];
    blue[1][n] = min(blue[0][n - 1], blue[2][n - 1]) + g[n];
    int min_blue = min(blue[0][n], blue[1][n]);
    int ans = min(min_red, min(min_green, min_blue));
    printf("%d\n", ans);
 
    return 0;
}
