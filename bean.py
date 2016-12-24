#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
http://yukicoder.me/problems/no/143
"""
def main():
	k, n, f = map(int, input().strip().split())
	ages = map(int, input().strip().split())
	sum_age = sum(ages)

	if(k * n) < sum_age:
		print(-1)
	else:
		print((k * n) - sum_age)


if __name__ == "__main__":
	main()
