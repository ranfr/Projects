#include<iostream>
#include<vector>


class Solution {
public:
    int candy(std::vector<int>& ratings) {
        std::vector<int> candy;
        candy.push_back(1);
        for (int i = 1; i < ratings.size(); ++i) {
            if (ratings[i] > ratings[i - 1]) {
                int temp = candy[i - 1] + 1;
                candy.push_back(temp);
            }
            else if (ratings[i] == ratings[i - 1]) {
                candy.push_back(1);
            }
            else {
                if (candy[i - 1] != 1) {
                    candy.push_back(1);
                }
                else {
                    int j = i - 1;
                    do {
                        ++candy[j];
                        --j;
                    } while ((j > -1) && (ratings[j] > ratings[j + 1]) && (candy[j] < candy[j - 1]));
                    candy.push_back(1);
                }
            }
        }
        int sum = 0;
        for (int c : candy) {
            sum += c;
        }
        return sum;
    }
};


int main(int argc, char *argv[]) {
    int n;
    std::cin >> n;
    std::vector<int> candy;
    for (int i = 0; i < n; ++i) {
        int temp;
        std::cin >> temp;
        candy.push_back(temp);
    }
    Solution solution;
    int sum = solution.candy(candy);
    std::cout << "sum: " << sum << std::endl;
    return 0;
}