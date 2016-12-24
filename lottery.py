#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
http://yukicoder.me/problems/no/128
"""

def main():
	n = int(input())
	m = int(input())
	if(n / m) < 1000:
		print(0)
	else:
		quo = ((n//m)//1000)
		mol = (n//m) - (quo * 1000)
		if mol == 0:
			print(n//m)
		else:
			print(n//m - mol)
 


if __name__ == '__main__':
	main()