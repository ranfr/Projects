#include<iostream>
#include<vector>


class Solution {
public:
    int canCompleteCircuit(std::vector<int>& gas, std::vector<int>& cost) {
        int len = gas.size();
        for (int i = 0; i < len; ++i) {
            int g = gas[i];
            bool ok = true;
            for (int j = i; j < len + i; ++j) {
                if (j > len - 1) {
                    g -= cost[j - len];
                }
                else {
                    g -= cost[j];
                }
                if (g < 0) {
                    ok = false;
                    break;
                }
                if (j > len - 2) {
                    g += gas[j + 1 - len];
                }
                else {
                    g += gas[j + 1];
                }
            }
            if (ok) return i;
        }
        return -1;
    }
};


int main(int argc, char *argv[]) {
    Solution solution;
    std::vector<int> gas, cost;
    int len;
    std::cin >> len;
    for (int i = 0; i < len; ++i) {
        int temp;
        std::cin >> temp;
        gas.push_back(temp);
    }
        for (int i = 0; i < len; ++i) {
        int temp;
        std::cin >> temp;
        cost.push_back(temp);
    }

    int index = solution.canCompleteCircuit(gas, cost);
    std::cout << index << std::endl;
    return 0;
}