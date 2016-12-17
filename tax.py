#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
yukicoder.me/problens/no/56
"""

def main():
	amount, tax = map(int, input().strip().split())
	print(int(amount * (tax * 0.01) + amount))
	

if __name__ == '__main__':
	main()
