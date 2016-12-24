#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
http://yukicoder.me/problems/no/275
"""

def main():
	n = int(input())
	nums = map(int, input().strip().split())

	if n % 2 == 1:
		print (sorted(nums)[n // 2])
	else:
		index = n // 2
		num = sorted(nums)
		median1 = num[index]
		median2 = num[index - 1]
		print((median1 + median2) / 2)


if __name__ == '__main__':
	main()