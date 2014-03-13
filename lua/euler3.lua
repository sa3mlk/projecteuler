#!/usr/bin/env lua

function isprime(p)
	local n = p / 2
	for i = 2, n do
		if math.fmod(p, i) == 0 then
			return false
		end
	end
	return true
end

function trial_div_prime(n)
	local max, res = math.sqrt(n), 0
	for i = 2, max do
		if math.fmod(n, i) == 0 and isprime(i) then
			res = i
		end
	end
	return res
end

print("Answer is " .. trial_div_prime(600851475143))
