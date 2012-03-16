#include <iostream>
#include <cmath>

template <typename T>
bool is_prime(T p)
{
	for (T i = 2; i < (p / 2.0); ++i)
		if (fmod(p, i) == 0.0)
			return false;
	return true;
}

template <typename T>
T trial_division_prime_only(T n)
{
	T max = sqrt(n), result = 0.0;
	for (T i = 2; i <= max; ++i)
		if (fmod(n, i) == 0.0 && is_prime(i))
			result = i;
	return result;
}

int main(int argc, char *argv[])
{
	long double n = 600851475143;
	std::cout << "Answer is " << trial_division_prime_only(n) << std::endl;
	return 0;
}

