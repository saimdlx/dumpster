#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int main()
{  
    vector<int> nums = {1,2,4,5};
    int k;
    unordered_map<int, int> count;
    int n = nums.size();
    for (int x : nums)
    {
        count[x]++;
    }
    if (k == 1)
    {

        int ans = -1;
        for (auto [val, freq] : count)
        {
            if (freq == 1 && val > ans)
            {
                ans = val;
            }
        }
        return ans;
    }
    else if (k == n)
    {
        sort(nums.begin(), nums.end());
        return nums[nums.size() - 1];
    }
    if (k > 1 && k < n)
    {
        bool cB = count[nums[0]] == 1;
        bool cE = count[nums[n - 1]] == 1;
        if (cB && cE)
        {
            return max(nums[0], nums[n - 1]);
        }
        if (cB)
        {
            return nums[0];
        }
        if (cE)
        {
            return nums[n - 1];
        }
        else
        {
            return -1;
        }
    }
    return 0;
}