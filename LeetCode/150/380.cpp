#include <iostream>
#include <vector>


class RandomizedSet {
    public:
        RandomizedSet() {
            vector_set.clear();
        }
        
        bool insert(int val) {
            bool insert = true;
            for (int param : vector_set) {
                if (param == val) {
                    insert = false;
                    break;
                }
            }
            vector_set.push_back(val);
            return insert;
        }
        
        bool remove(int val) {
            bool removable = false;
            for (int i = 0; i < vector_set.size(); ++i) {
                if (vector_set[i] == val) {
                    removable = true;
                    vector_set.erase(vector_set.begin() + i);
                    break;
                }
            }
            return removable;
        }
        
        int getRandom() {
            int num = vector_set.size();
            int index = 0;
            if (num > 0) index = rand() % num;
            return vector_set[index];
        }
        private:
            std::vector<int> vector_set;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */

int main (int argc, char *argv[]) {
    RandomizedSet random_set;
    bool b1 = random_set.insert(1);
    std::cout << b1 << std::endl;
    bool b2 = random_set.remove(2);
    std::cout << b2 << std::endl;
    bool b3 = random_set.insert(2);
    std::cout << b3 << std::endl;
    return 0;
}