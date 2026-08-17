#include <iostream>
#include <vector>
#include <algorithm>


int main(){
    std::vector<char> s = {'h','e','l','l','o'};
    int n = s.size();
    int start = 0;
    int end = n - 1;
    while (start<end){
        std::swap(s[start], s[end]);
        start++;
        end--;
    }
    for (char i : s){
        std::cout << i << " ";
    }
    return 0;
}