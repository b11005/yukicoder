#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
http://yukicoder.me/problems/no/441
"""
def main():
    n, m = map(int, input().strip().split())
    
    if (n * m) > (n + m):
        print('P')
    elif (n * m) == (n + m):
    	print('E')
    else:
        print('S')

if __name__ == "__main__":
    main()
