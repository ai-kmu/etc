#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool mapp[51][51];          // 변환 가능한 단어를 나타내는 인접행렬
bool visit[51];             // 방문했던 노트 check
const int INF = 99999;

int mapping(string& begin, string& target, vector<string>& words) {
    words.push_back(begin);
    int targetIdx = -1;
    for (int ni = 0; ni < words.size(); ++ni) {
        if (targetIdx == -1 && words[ni].compare(target) == 0) {
            targetIdx = ni;
        }
        for (int ti = 0; ti < words.size(); ++ti) {
            string nowWord = words[ni];
            string targetWord = words[ti];
            if (nowWord.compare(targetWord) != 0) {
                bool wordCheck = false;
                for (int wi = 0; wi < nowWord.size(); ++wi) {
                    // 한 글자만 다를 때 ture로 체크 !
                    if (nowWord[wi] != targetWord[wi]) {
                        if (wordCheck) {
                            wordCheck = false;
                            break;
                        }
                        wordCheck = true;
                    }
                }
                if (wordCheck) {
                    mapp[ni][ti] = true;
                }
            }
        }
    }
    return targetIdx;
}
int count(int nowWord, int targetWord, int level, int length) {
    if (targetWord == -1) {
        return 0;
    }
    if (nowWord == targetWord) {
        return level;
    }
    visit[nowWord] = true;
    int minn = INF;
    for (int wi = 0; wi < length; ++wi) {
        if (mapp[nowWord][wi] && !visit[wi]) {
            // 깊이 우선 탐색하면서 반환된 트리의 레벨 중 가장 작은 것을 반환함.
            minn = min(count(wi, targetWord, level + 1, length), minn);
        }
    }
    visit[nowWord] = false;
    return minn;
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    int length = words.size();
    int targetIdx = mapping(begin, target, words);
    answer = count(length, targetIdx, 0, length + 1);
    if (answer == INF)
        answer = 0;
    return answer;
}
