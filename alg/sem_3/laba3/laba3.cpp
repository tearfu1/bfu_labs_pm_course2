#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int x = 0;
    std::cin >> x;
    std::vector<int> numbers(0);

    if (x == 1)
    {
        numbers.push_back(1);
    }

    float log3x = log(x) / log(3);
    float log5x = log(x) / log(5);
    float log7x = log(x) / log(7);

    for (int k = 0; k < log3x; ++k) 
    {
        for (int l = 0; l < log5x;++l)
        {
            for (int m = 0; m < log7x; ++m)
            {
                int res = pow(3, k) * pow(5, l) * pow(7, m);
                if (res <= x) numbers.push_back(res);
            }
        }
    }
    
    std::sort(numbers.begin(), numbers.end());

    for (int i = 0; i < numbers.size(); ++i)
    {
        std::cout << numbers[i] << " ";
    }
    return 0;
}