#include <algorithm>
#include <iostream>

int main(int argc, char *argv[])
{
	int numbers[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

	for (size_t i = 0; i < 999999; ++i)
		std::next_permutation(numbers, numbers + 10);

	std::cout << "The millionth permutation is: ";
	for (size_t i = 0; i < sizeof(numbers) / sizeof(numbers[0]); ++i)
		std::cout << numbers[i];
	std::cout << std::endl;

	return 0;
}
