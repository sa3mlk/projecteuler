#include <iostream>
#include <utility>

template <typename T>
inline T next_seq(T n)
{
	return n & 1 ? (n * 3) + 1 : n / 2;
}

template <typename T>
inline T chain_length(T n)
{
	T i;
	for (i = 1; n != 1; ++i)
		n = next_seq(n);
	return i;
}

int main(int argc, char *argv[])
{
	std::pair<uint64_t, uint64_t> chain_pair;
	for (uint64_t i = 2; i < 1000000; ++i)
	{
		uint64_t len = chain_length(i);
		if (len > chain_pair.first)
			chain_pair = std::make_pair(len, i);
	}

	std::cout << "Answer is "
			  << chain_pair.first
			  << " for n = "
			  << chain_pair.second
			  << std::endl;

	return 0;
}
