#include <fstream>
#include <vector>
#include <map>
#include <algorithm>

std::ifstream fin("day1.in");
std::ofstream fout("day1.out");

std::vector<int> left;

void solve1() {
    std::vector<int> right;
    int x;
    while (fin >> x) {
        left.push_back(x);
        fin >> x;
        right.push_back(x);
    }
    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());
    int ssize = left.size();
    long long ans = 0;
    for (int i = 0; i < ssize; i++) {
        ans += std::abs(left[i] - right[i]);
    }
    fout << ans;
}

void solve2() {
    std::map<int, int> right;
    std::vector<int> left;
    int a;
    while (fin >> a) {
        left.push_back(a);
        fin >> a;
        right[a]++;
    }
    long long score = 0;
    for (auto &x : left) {
        score += x * (long long)right[x];
    }
    fout << score;
}

int main() {
    int task = 2;

    if (task == 1) solve1();
    else solve2();
    return 0;
}
