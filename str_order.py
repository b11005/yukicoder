#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
http://yukicoder.me/problems/no/69
"""

def main():
	a = input()
	b = input()
	
	if sorted(a) == sorted(b):
		print('YES')
	else:
		print('NO')


if __name__ == '__main__':
	main()