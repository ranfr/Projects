#include <iostream>
#include <vector>


class Solution {
    public:
        int maxProfit(std::vector<int>& prices) {
            int temp = prices[0];
            int price = 0;
            for (int p : prices) {
                if (p > temp) {
                    price += p - temp;
                    temp = p;
                }
                else {
                    temp = p;
                }
            }
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