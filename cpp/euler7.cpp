#include <iostream>

template <typename T>
inline bool is_prime(T p)
{
	for (T i = 2; i < p; ++i)
		if (!(p % i))
			return false;
	return true;
}

int main(int argc, char *argv[])
{
	int n = 10001; 
	for (int pnum = 0, i = 2;; ++i)
	{
		if (is_prime(i))
		{
			pnum++;
			if (pnum == n)
			{
				std::cout << "Answer is " << i << std::endl;
				return 0;
			}
		}
	}
}

