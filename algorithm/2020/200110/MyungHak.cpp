#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int line_num;
	cin >> line_num;

	vector<pair<long long int, long long int>> line;

	long long int start, end;
	for (int i = 0; i < line_num; i++) {
		cin >> start >> end;
		line.emplace_back(start, end);
	}
	sort(line.begin(), line.end(), greater<pair<int, int>>());

	long long int start_line[2] = { -1000000001, -1000000001 };
	long long int line_length = 0;

	while (!line.empty()) {
		auto current = line.back();
		line.pop_back();
		start = current.first;
		end = current.second;

		if (start > end) {
			long long int T = start;
			start = end;
			end = T;
		}

		if (start_line[0] <= start && end <= start_line[1]) {
			continue;
		}

		line_length += (end - start);
		
		if (start < start_line[1]) {
			line_length -= start_line[1] - start;
		}
		start_line[0] = start;
		start_line[1] = end;
	}

	cout << line_length;

	return 0;
}
