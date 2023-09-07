#include <iostream>
#include <vector>


class Solution {
    public:
        int removeDuplicates(std::vector<int>& nums) {
            int n_size = nums.size();
            if (n_size < 3) {
                return n_size;
            }
            int p = 2, q = 2;
            while (q < n_size) {
                if (nums[p - 2] != nums[q]) {
                    nums[p] = nums[q];
                    ++p;
                }
                ++q;
            }
            return p;
        }
};


int main (int argc, char* argv[]) {
    Solution solution;
    std::vector<int> v;
    int n;
    std::cin >> n;
    for (int i=0; i<n; ++i) {
        int temp;
        std::cin >> temp;
        v.push_back(temp);
    }
    int ti = solution.removeDuplicates(v);
    for (int i=0; i<ti; ++i) {
        std::cout << v[i] << ' ';
    }
    std::cout << std::endl;
    return 0;
}