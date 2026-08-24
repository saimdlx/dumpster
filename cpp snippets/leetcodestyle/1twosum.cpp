/*
        Primitive O(n^2) solution
        for (int i = 0 ; i < nums.size() ; i++){
            for (int j = i + 1; j < nums.size(); j++){
                if (nums[i] + nums[j] == target){
                    return {i,j};
                }
            }
        }
        return {0,0};
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hmap;
        for (int i = 0 ; i < nums.size() ; i++){
            int key = target - nums[i];
            if (hmap.count(key)){
                return {hmap[key], i};
            }
            hmap[nums[i]] = i;
        }
        return {};
    }
};
