#!/usr/bin/env lua

function fib(n)
	local a, b = 1, 0
	for i = 1, n do a, b = a + b, a end
	return a
end

sum, i = 0, 2
while true do
	f = fib(i)
	if f > 4e6 then break end
	i = i + 1
	if f % 2 == 0 then sum = sum + f end
end

print("Answer is " .. sum)
