#!/usr/bin/env lua

function is_palindrome(candidate)
	local n, reversed = candidate, 0
	while n > 0 do
		reversed = reversed * 10 + n % 10
		n = math.floor(n / 10)
	end
	return candidate == reversed
end

function euler4()
	local min, max, largest = 100, 1000, 0
	for x = min, max do
		for y = min, max do
			if is_palindrome(x * y) then
				local product = x * y
				if product > largest then
					largest = product
				end
			end
		end
	end

	return largest
end

print("Answer is " .. euler4())
