#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
//#define TEST

//아이디어 시간 : 
//구현 시간 : 
//총 시간 : 

//std::fstream ifStream;

void Solution()
{
	int cases;
	//ifStream >> cases;
	std::cin >> cases;

	//색깔비용 원본 저장
	std::vector<std::vector<int>> doublearray(cases,std::vector<int>(3,0));
	//계산용
	std::vector<std::vector<int>> doublearrayCopy(cases, std::vector<int>(3, 0));

	//데이터 받기
	for (int i = 0; i < cases; ++i)
	{
		for (int j = 0; j < 3; ++j)
		{
			int tmp;
			//ifStream >> tmp;
			std::cin >> tmp;
			doublearray[i][j] = tmp;
		}
	}

	//0번째 줄 집의 색깔 하나를 기준으로  만들기 위해 나머지 두 집에 max값  넣어줄때사용
	int max = 1000 * cases - +1;

	//최소 값 계산용(답)
	int min = 10000000;

	for (int i = 0; i < 3; ++i)
	{
		//집 기준 바뀔 때마다 집 비용계산용 배열 초기화 
		for (int x = 0; x < cases; ++x)
		{
			for (int y = 0; y < cases; ++y)
			{
				doublearrayCopy[x][y] = doublearray[x][y];
			}
		}

		//0번째 줄 집의 색깔 하나를 기준으로  만들기 위해 나머지 두 집에 max값  넣어줌
		for (int j = 0; j < cases; ++j)
		{
			if (j != i)
			{
				doublearrayCopy[0][j] = max;
			}			
		}		

		//집 비용 더하는 과정
		for (int m = 1; m < cases; ++m)
		{
			doublearrayCopy[m][0] += std::min(doublearrayCopy[m - 1][1], doublearrayCopy[m - 1][2]);
			doublearrayCopy[m][1] += std::min(doublearrayCopy[m - 1][0], doublearrayCopy[m - 1][2]);
			doublearrayCopy[m][2] += std::min(doublearrayCopy[m - 1][0], doublearrayCopy[m - 1][1]);
		}

		//다 계산하고 마지막 줄의 집 색깔 비용중 가장 낮은거 하고 지금까지 비용 낮은거 하고 비교
		for (int z = 0; z < 3; ++z)
		{
			
			if (doublearrayCopy[cases-1][z] < min && i!=z)
			{
				min = doublearrayCopy[cases - 1][z];
			}
		}
	}

	

	std::cout << min << std::endl;
	
	
}

int main(void)
{
//#ifdef TEST
//	ifStream.open("Input.txt");
//#endif
	Solution();

	return 0;
}
