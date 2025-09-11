#include <vector>
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            vector<int> res;    
            int len = nums.size();        

            // calculate the list of prefix
            vector<int> prefix;
            int aux_prefix = 1;
            for (int i = 0; i < len; i++){
                prefix.push_back(aux_prefix);
                aux_prefix *= nums[i];
            }
            // calculate the list of sufix
            vector<int> sufix;
            int aux_sufix = 1;
            for(int i = len - 1; i > 0 ; i--){
                sufix.push_back(aux_sufix);
                aux_sufix *= nums[i];
            }

            for(int i = 0; i < len; i++){
                res.push_back(prefix[i] * prefix[i]);
            }
            return res;
        }
};