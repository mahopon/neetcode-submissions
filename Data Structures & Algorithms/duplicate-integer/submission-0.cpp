class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> sInt;
        for (int i = 0; i < nums.size(); i++) {
            if (!(sInt.insert(nums[i]).second)) return 1;
        }

        return 0;
    }
};
