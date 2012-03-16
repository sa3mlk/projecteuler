using System.Collections.Generic;

namespace Common
{
	public static class Generators
	{
		public static IEnumerable<int> NumberSequence(int from, int to)
		{
			do
			{
				yield return from++;
			} while (from < to);
		}
	}
}
