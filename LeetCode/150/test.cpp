#include<iostream>
#include<map>


int main(int argc, char* argv[]) {
    std::map<int, int> cnts;
    int num;
    std::cin >> num;
    ++cnts[num];
    std::cout << cnts[num] << std::endl;
    return 0;
}