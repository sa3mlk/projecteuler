// Add all the natural numbers below one thousand that are multiples of 3 or 5.
class Euler1 {

	private static int sumMultiples(int n)
	{
		if (n == 0)
			return 0;
		else
			return ((n % 3) == 0 || (n % 5) == 0) ?
				n + sumMultiples(n - 1) :
				0 + sumMultiples(n - 1);
	}

	public static void main(String[] args) {
		System.out.println("Answer is " + sumMultiples(1000));
	}	

}

