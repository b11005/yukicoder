#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
http://yukicoder.me/problems/no/163
"""

def main():
	caps = input()
	result = []
	for cap in caps:
		if cap.isupper():
			result.append(cap.lower())
		else:
			result.append(cap.upper())
	print(''.join(result))


if __name__ == '__main__':
	main()