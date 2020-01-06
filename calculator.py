
import math

bracket = {10000: 0.512, 5001: 0.452, 2501: 0.254, 1001: 0.128, 501: 0.053}

def calc(inp):
	y = [i for i in bracket.keys() if i <= inp]

	out = 0
	for i in y:
		new = inp - i
		out += new * bracket[i]
		inp -= new

	return out

while True:
	inp = int(input("> "))
	if inp > 500:
		print(math.ceil(calc(inp)))
	else:
		print("Receives Grant")