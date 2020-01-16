#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int line_cnt;
	scanf("%d", &line_cnt);
	vector<pair<int, int>> points(line_cnt);

	for (int i = 0; i < line_cnt; i++)
	{
		scanf("%d %d", &points[i].first, &points[i].second);
		if (points[i].first > points[i].second)
			swap(points[i].first, points[i].second);
	}

	sort(points.begin(), points.end());
	int left = points[0].first, right = points[0].second;
	int line_length = 0;
	for (int i = 1; i < line_cnt; i++)
	{
		if (points[i].first <= right)
		{
			right = max(points[i].second, right);
		}
		else
		{
			line_length += right - left;
			left = points[i].first;
			right = points[i].second;
		}
	}
	
	line_length += right - left;
	printf("%d\n", line_length);
	return 0;
}