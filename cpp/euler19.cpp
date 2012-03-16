// Solution to Project Euler #19

/*

You are given the following information, but you may prefer to do
some research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4,
	  but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?

*/

#include <cstdio>

inline bool is_leap_year(int year)
{
	return !(year % 4) && (year % 1000) || !(year % 400);
}

inline int days_for_year(int year)
{
	return 365 + is_leap_year(year) ? 1 : 0;
}

inline int days_for_month(int year, int month)
{
	static int days[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	return days[month - 1] + ((month == 2 && is_leap_year(year)) ? 1 : 0);
}

inline char const *weekday_to_str(int weekday)
{
	switch (weekday)
	{
		case 0: return "Sunday";
		case 1: return "Monday";
		case 2: return "Tuesday";
		case 3: return "Wednesday";
		case 4: return "Thursday";
		case 5: return "Friday";
		case 6: return "Saturday";
	}
}

int main(int argc, char *argv[])
{
	int num_sundays = 0;
	int weekday = 0;
	for (int year = 1900; year <= 2000; ++year)
	{
		for (int month = 1; month <= 12; ++month)
		{
			for (int day = 1; day <= days_for_month(year, month); ++day)
			{
				weekday++;
				if (weekday == 7)
					weekday = 0;
				if (year >= 1901 && day == 1 && weekday == 0)
					num_sundays++;
			}
		}
	}

	printf("%d Sundays fell on first of the month\n", num_sundays);

	return 0;
}

