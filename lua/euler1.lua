#!/usr/bin/env lua

function sum(a)
	local sum = 0;
	for i = 0, 999, a do sum = sum + i end
	return sum
end

print("Answer is " .. sum(3) + sum(5) - sum(15))

