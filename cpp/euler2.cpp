// Solution to Project Euler #2
#include <iostream>

int main(int argc, char *argv[])
{
	int sum = 0;
	for (int t, c = 2, p = 1; sum < 4000000; )
	{
		if (!(c & 1))
			sum += c;
		t = c; c += p; p = t;
	}

	std::cout << "Answer is " << sum << std::endl;

	return 0;
}
