#include <iostream>

template <typename T>
bool is_palindrome(T candidate)
{
	T n = candidate, rev = 0;
	while (n > 0)
	{
		rev = rev * 10 + n % 10;
		n /= 10;
	}
	return candidate == rev;
}

int main(int argc, char *argv[])
{
	int largest_palindrome = 0, cx, cy;
	int max = 1000, min = 100;
	for (int x = min; x < max; ++x)
	{
		for (int y = min; y < max; ++y)
		{
			if (is_palindrome(x * y))
			{
				int product = x * y;
				if (product > largest_palindrome)
				{
					cx = x; cy = y;
					largest_palindrome = product;
				}
			}
		}
	}
	std::cout << "Answer is "
			  << largest_palindrome
			  << " (" << cx << " * " << cy << ")"
			  << std::endl;
	return 0;
}

