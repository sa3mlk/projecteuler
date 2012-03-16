#include <iostream>

template <typename T>
T sum_square(T n)
{
	T result = 0;
	for (T i = 1; i <= n; ++i)
		result += i * i;
	return result;
}

template <typename T>
T square_sum(T n)
{
	T result = 0;
	for (T i = 1; i <= n; ++i)
		result += i;
	return result * result;
}

int main(int argc, char *argv[])
{
	int n = 100;
	std::cout << "Answer is "
			  << square_sum(n) - sum_square(n)
			  << std::endl;
	return 0;
}

