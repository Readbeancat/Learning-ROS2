#include <iostream>
#include <algorithm>


int main(){

    auto add = [](int x, int y) -> int { return x + y; };
    int sum = add(5, 3);
    auto p_sum = [sum]() -> void 
    { std::cout << "sum: " << sum << std::endl; 
    };
    p_sum();
    return 0;
}

 