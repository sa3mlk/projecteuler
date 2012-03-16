// Solution to Project Euler #5
#include <iostream>

bool f(int n)
{
	for (int i = 1; i <= 20; ++i)
		if (n % i)
			return false;
	return true;
}

int main(int argc, char *argv[])
{
	int n = 1;
	while (!f(n))
		++n;

	std::cout << "Answer is " << n << std::endl;
	return 0;
}
