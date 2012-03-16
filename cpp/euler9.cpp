#include <iostream>

template <typename T>
T triplet_sum(T k, T m, T n, T &product)
{
	T a = k * (2 * m * n);
	T b = k * ((m * m) - (n * n));
	T c = k * ((m * m) + (n * n));
	product = a * b * c;
	return a + b + c;
}

int problem9()
{
	int p;
	for (int k = 1; k < 100; ++k)
		for (int n = 1; n < 100; ++n)
			for (int m = n + 1; m < 100; ++m)
				if (triplet_sum(k, m, n, p) == 1000)
					return p;
}

int main(int argc, char *argv[])
{
	std::cout << "Answer is " << problem9() << std::endl;
	return 0;
}
