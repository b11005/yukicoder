#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
http://yukicoder.me/problems/no/47
"""

def main():
	num = int(input())
	now = 1
	counter = 0
	while(num > now):
		now = now * 2
		counter += 1
	print (counter)


if __name__ == "__main__":
	main()