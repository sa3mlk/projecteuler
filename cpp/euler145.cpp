/* Problem 145
 *
 * Some positive integers n have the property that the sum [ n + reverse(n) ]
 * consists entirely of odd (decimal) digits. For instance,
 * 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible;
 * so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in
 * either n or reverse(n).
 *
 * There are 120 reversible numbers below one-thousand.
 *
 * How many reversible numbers are there below one-billion (10^(9))?
 *
 */

#include <iostream>

template <typename T>
inline T reverse(T n)
{
	T r = 0;
	while (n > 0)
	{
		r = r + n % 10;
		n /= 10;
		r *= 10;
	}
	return r / 10;
}

template <typename T>
inline T is_all_odd(T n)
{
	for (; n > 0; n /= 10)
		if (!(n & 1)) return 0;
	return 1;
}

template <typename T>
inline T is_reversible(T n)
{
	if (n % 10 == 0) return 0;
	T r = reverse(n);
	if (r % 10 == 0) return 0;
	if ((r + n) & 1 == 0) return 0;
	else return is_all_odd(n + r);
}

int main(int argc, char *argv[])
{
	unsigned long long num_reversible = 0;
	for (unsigned long long i = 0; i < 1000000000; ++i)
		num_reversible += is_reversible(i);

	std::cout << "Answer is " << num_reversible << std::endl;

	return 0;
}

