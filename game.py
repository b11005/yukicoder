#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
http://yukicoder.me/problems/no/264
"""

def main():
    n, k = map(int, input().strip().split())
    if n == k:
    	print('Drew')
    elif (n == 0 and k == 1) or (n == 1 and k == 2) or (n == 2 and k == 0):
    	print('Won')
    else:
    	print('Lost')


if __name__ == '__main__':
    main()
