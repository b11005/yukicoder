#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
yukicoder.me/problems/no/5
"""

def main():
    width = int(input())
    _ = int(input())
    blocks = sorted([int(block) for block in input().split()])
    total = []
    for block in blocks:
    	if width >= (sum(total) + block):
    		total.append(block)
    print (len(total))


if __name__ == '__main__':
    main()
