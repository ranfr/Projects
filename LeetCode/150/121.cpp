#include <iostream>
#include <vector>


class Solution {
    public:
        int maxProfit(std::vector<int>& prices) {
            int price = 0;
            int *dp = new int [prices.size()];
            dp[0] = prices[0];
            for (int i=1; i<prices.size(); ++i) {
                dp[i] = std::min(dp[i-1], prices[i]);
                price = std::max(prices[i]-dp[i], price);
            }
            delete [] dp;
            return price;
        }
};


int main(int argc, char *argv[]) {
    Solution solution;
    int num;
    std::cin >> num;
    std::vector<int> prices;
    for (int i=0; i<num; ++i) {
        int temp;
        std::cin >> temp;
        prices.push_back(temp);
    }
    int price = solution.maxProfit(prices);
    std::cout << price << std::endl;
    return 0;
}