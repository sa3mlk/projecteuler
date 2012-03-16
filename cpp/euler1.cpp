// Solution to Project Euler #1
#include <iostream>

int f(int n)
{
	if (!n)
		return 0;
	else
		return (!(n % 3) || !(n % 5)) ? n + f(n - 1) : 0 + f(n - 1);
}

int main(int argc, char *argv[])
{
	int n = 1000 - 1;
	std::cout << "Answer is " << f(n) << std::endl;
	return 0;
}
