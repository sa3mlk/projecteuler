#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

static const char cipherdata[] = {
	#include "../data/euler59.txt"
};

#define lengthof(T) (sizeof(T) / sizeof(T[0]))

using std::vector;
using std::cout;
using std::string;
using std::count_if;
using std::accumulate;

typedef vector<string> key_vector;

inline char *next_key(char *k)
{
	k[2]++;
	if (k[2] > 'z')
	{
		k[1]++; k[2] = 'a';
		if (k[1] > 'z')
		{
			k[0]++; k[1] = 'a';
		}
	}

	return k;
}

inline void generate_keys(key_vector &keys)
{
	char k[4] = "aaa";
	static const size_t length = 26 * 26 * 26;
	keys.resize(length);
	keys[0] = k;
	for (size_t i = 1; i != length; ++i)
		keys[i] = next_key(k);
}

inline string decrypt(char const *ct, string const &key, size_t length)
{
	string pt;
	size_t key_length = key.length();
	pt.resize(length);
	for (size_t i = 0; i != length; i++)
		pt[i] = ct[i] ^ key[i % key_length];

	return pt;
}

inline bool common_letter(char c)
{
	return c == ' ' || c == 'e' || c == 't' || c == 'a' || c == 'o' || c == 'i';
}

int main(int argc, char *argv[])
{
	key_vector all_keys, possible_keys;
	generate_keys(all_keys);

	static const char *words[] = { "The ", "the ", "and ", "this " };
	for (key_vector::const_iterator it = all_keys.begin(); it != all_keys.end(); ++it)
	{
		string pt = decrypt(cipherdata, *it, 64);
		for (size_t j = 0; j != lengthof(words); ++j)
		{
			if (string::npos != pt.find(words[j]))
			{
				possible_keys.push_back(*it);
				break;
			}
		}
	}

	cout << "Trying " << possible_keys.size() << " possible keys.\n";

	string most_probable_key;
	int most_common_letters = 0;
	for (key_vector::const_iterator it = possible_keys.begin(); it != possible_keys.end(); ++it)
	{
		string pt = decrypt(cipherdata, *it, sizeof(cipherdata));
		int common_letters = count_if(pt.begin(), pt.end(), common_letter);
		if (common_letters > most_common_letters)
		{
			most_common_letters = common_letters;
			most_probable_key = *it;
		}
	}

	string pt = decrypt(cipherdata, most_probable_key, sizeof(cipherdata));
	cout << "Decrypting with most probable key \"" << most_probable_key.c_str() << "\":  " << pt.c_str() << "\n";
	cout << "ASCII sum: " << accumulate(pt.begin(), pt.end(), 0) << "\n";

	return 0;
}

