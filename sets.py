# -*- coding: UTF-8 -*-

def main():
	s = set([1, 2, 3])
	t = set([3, 4, 5])

	print("La intersección entre las dos listas es: {}".format(s.intersection(t)))
	print("La diferencia entre las dos listas es: {}".format(s.difference(t)))
	print("La union entre las dos listas es: {}".format(s.union(t)))

if __name__ == '__main__':
	main()