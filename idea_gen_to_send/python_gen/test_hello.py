import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("arguments", nargs="+")
	args = parser.parse_args()
	out_string=list();
	for st in args.arguments:
		out_string.append(st);
	print(out_string);