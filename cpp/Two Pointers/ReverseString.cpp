#include <vector>
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

class Solution {
public:
   void reverseString(vector<char>& s) {
      for(int i = 0 ; i < s.size() / 2; i++){
         int end_idx = s.size() - 1 - i;
         char aux_s = s[i];   
         s[i] = s[end_idx];
         s[end_idx] = aux_s;
      }
   }
}; 