using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Common;

namespace ProjectEuler
{
	class Euler1
	{
		static void Main(string[] args)
		{
			var nums = from n in Generators.NumberSequence(0, 1000)
				where ((n % 3 == 0) || (n % 5 == 0)) select n;
			Console.WriteLine("Answer is {0}", nums.Sum());
		}

	}
}
