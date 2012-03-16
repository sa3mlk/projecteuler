// Solution to Project Euler #5
#include <iostream>
#include <cmath>

int main(int argc, char *argv[])
{
	long long answer = 0;
	long double f = pow(2.0, 16);
	std::cout << f << std::endl;
	while (f > 1.0)
	{
		answer += static_cast<int>(fmod(f, 10));
		f = f / 10.0;
	}
	std::cout << "Answer is " << answer << std::endl;
	return 0;
}
