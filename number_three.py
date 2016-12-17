#!/usr/bin/env python3
# -*- coding; utf-8 -*-

"""
yukicoder.me/problens/no/207
"""

def main():
	start, end = map(int, input().split())
	for number in range(start, end + 1):
		if number % 3 == 0:
			print(number)
			continue
		if '3' in str(number):
			print(number)


if __name__ == '__main__':
	main()