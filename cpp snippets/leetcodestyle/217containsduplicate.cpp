#include <set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> dups(nums.begin(), nums.end());
        if (nums.size() != dups.size()){
            return true;
        }
        return false;
    }
};